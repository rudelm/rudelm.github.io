---
author: Centurio
categories:
- Linux
- NAS
- Raspberry Pi
date: "2021-11-30T22:14:13Z"
guid: https://centurio.net/?p=3393
id: 3393
tags:
- HyperBackup
- minio
- Synology
title: Setup minio as backup target for Synology HyperBackup
url: /2021/11/30/setup-minio-as-backup-target-for-synology-hyperbackup/
---
# Introduction
After some unsuccessful <a href="https://centurio.net/2020/09/26/setup-wireguard-vpn-on-raspbian/" data-type="post" data-id="3386">tests with WireGuard VPN</a>, I've tried something new to provide a suitable encrypted backup target for my Synology NAS.

Minio is a block storage server which is compatible to AWS S3 API. That means I can configure a S3 compatible target in HyperBackup. Here's now a small [installation guide](https://computingforgeeks.com/how-to-setup-s3-compatible-object-storage-server-with-minio/) for a Raspberry Pi, which I've modified for my needs:

## Installation
Download a copy of minio for arm and make it executable:

```
wget https://dl.minio.io/server/minio/release/linux-arm/minio
chmod +x minio
sudo mv minio /usr/local/bin/
```

We need a user for the minio process to run:

```
sudo groupadd --system minio
sudo useradd -s /sbin/nologin --system -g minio minio
```

We need to give ownership of the minio working directory:

```
sudo chown -R minio:minio /data/
```

## Configuration
Now we configure a service for starting minio using [Systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md), writing the following lines into /etc/systemd/system/minio.service. Make sure to set the right working directory.

```
[Unit]
Description=Minio
Documentation=https://docs.minio.io
Wants=network-online.target
After=network-online.target
AssertFileIsExecutable=/usr/local/bin/minio

[Service]
WorkingDirectory=/data
User=minio
Group=minio

EnvironmentFile=-/etc/default/minio
ExecStartPre=/bin/bash -c "if [ -z \"${MINIO_VOLUMES}\" ]; then echo \"Variable MINIO_VOLUMES not set in /etc/default/minio\"; exit 1; fi"

ExecStart=/usr/local/bin/minio server $MINIO_OPTS $MINIO_VOLUMES

# Let systemd restart this service always
Restart=always

# Specifies the maximum file descriptor number that can be opened by this process
LimitNOFILE=65536

# Disable timeout logic and wait until process is stopped
TimeoutStopSec=infinity
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
```

Create a minio environment file in /etc/default/minio. This setups the credentials for minio (access key and secret key), as well as the volume (same as the working directory). I've added a parameter for the URL under which minio will be reachable (MINIO_DOMAIN) as well as a parameter to the options on where the certificates for TLS encryption should reside (-certs-dir):

```

# Volume to be used for Minio server.
MINIO_VOLUMES="/data"
# Use if you want to run Minio on a custom port
MINIO_OPTS="--certs-dir /data/.minio/certs --address :443"
# Access Key of the server.
MINIO_ACCESS_KEY=&lt;someAccessKey&gt;
# Secret key of the server.
MINIO_SECRET_KEY=&lt;someSecretKey&gt;
# Server Domain
MINIO_DOMAIN=&lt;domain&gt;
```

Reload systemd:

```
sudo systemctl daemon-reload
```

If you want to have minio starting at system startup:

```
sudo systemctl enable minio
```

## TLS encryption and lets encrypt
You should enable TLS by placing a private key, a certificate and eventually a CA certificate into the path supplied by the -certs-dir parameter. In my example it would be /data/.minio/certs. You can read more about securing minio with certificates under [this link](https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls).

I've started with the creation of a wildcard certificate created by my own trusted CA. However, you could create the same result by using Lets Encrypt. It's important to use a wildcard certificate, as this is a requirement for using [minio as backup target with Hyper Backup](https://itrandomness.com/2020/05/local-backups-with-synology-hyper-backup-and-minio/){.broken_link}. We'll run minio in [virtual-host-style requests](https://docs.min.io/docs/minio-server-configuration-guide.html). That's also the reason why you'll need to define the MINIO_DOMAIN variable.

Instead of adding the bucket name to the server domain, the bucket name will be put in front of the server domain. So you'll end up with domains like bucket.<domain> instead of <domain>/bucket. This is the reason why you'll need a wildcard certificate for the given domain.

As I'm using all-inkl as hosting provider, I was keen to know if I could use Let's Encrypt wildcard certificates in combination with the DDNS solution offered. However, for using Let's encrypt certificates, you'll need access to your domains DNS records and need to have a way to update TXT records, as the certs will automatically expire after 90 days. The general setup in combination with all-inkl is explained [here](https://stevenschwenke.de/GeneratingTLSCertificatesUsingCertbotManualModeAndDNSChallengeAndSetupWithAllInkl).

This was also the place, where I found [kasserver](https://github.com/fetzerch/kasserver). kasserver provides an interface to the adminstration interface of all-inkl. It's especially useful for setting up Let's encrypt certs using [certbot](https://github.com/fetzerch/kasserver#kasserver-dns-certbot).

Install it with

```
pip3 install kasserver
```

Setup the KAS credentials in ~/.netrc

```
machine kasapi.kasserver.com
login USERNAME
password PASSWORD
```

Restrict access to the file to only your user

```
chmod 600 ~/.netrc
```

Install certbot

```
sudo apt-get install certbot
```

Setup a user and folder for certbot

```
sudo groupadd --system letsencrypt
sudo useradd -s /sbin/nologin --system -g letsencrypt letsencrypt
sudo mkdir -p /etc/letsencrypt
sudo chown -R letsencrypt:letsencrypt /etc/letsencrypt
sudo mkdir -p /var/log/letsencrypt
sudo chown -R letsencrypt:letsencrypt /var/log/letsencrypt
sudo mkdir -p /var/lib/letsencrypt
sudo chown -R letsencrypt:letsencrypt /var/lib/letsencrypt
sudo usermod -a -G letsencrypt pi

mkdir ~/letsencrypt
mkdir ~/letsencrypt/config
mkdir ~/letsencrypt/work
mkdir ~/letsencrypt/logs

```

Request a certificate

```
certbot certonly -d subdomain.domain.com --config-dir /home/pi/letsencrypt/config --work-dir /home/pi/letsencrypt/work --logs-dir /home/pi/letsencrypt/logs --preferred-challenges dns --manual --manual-auth-hook /home/pi/.local/bin/kasserver-dns-certbot --manual-cleanup-hook /home/pi/.local/bin/kasserver-dns-certbot -m system@rudel.email
```

## Restart and testing

You can start minio using:

```
sudo systemctl start minio
```

Once it is started, you can reach it via https://[serverip|localhost]:9000. You can login to the web interface using the two keys defined in the /etc/default/minio file.

Create a new bucket. You'll use this bucket as your backup target in Hyper Backup.

The setup of Hyper Backup with S3 compatible providers is explained [here](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Backup/How_to_back_up_your_data_to_cloud_services_with_Hyper_Backup).