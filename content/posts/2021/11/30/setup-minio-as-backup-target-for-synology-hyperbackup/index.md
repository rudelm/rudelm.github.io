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

---
# Introduction
After some unsuccessful [tests with WireGuard VPN]({{< ref "/posts/2020/09/26/setup-wireguard-vpn-on-raspbian/">}}), I've tried something new to provide a suitable encrypted backup target for my Synology NAS.

Minio is a block storage server which is compatible to AWS S3 API. That means I can configure a S3 compatible target in HyperBackup. Here's now a small [installation guide](https://computingforgeeks.com/how-to-setup-s3-compatible-object-storage-server-with-minio/) for a Raspberry Pi, which I've modified for my needs:

## Installation
Download a copy of minio for arm and make it executable:

```bash
wget https://dl.minio.io/server/minio/release/linux-arm/minio
chmod +x minio
sudo mv minio /usr/local/bin/
```

Be aware that this download is sometimes very slow, especially from Europ. There's an [open issue](https://github.com/minio/minio/issues/9847) but looks like the conversation is locked and no one was able to complain about it again.

We need a user for the minio process to run:

```bash
sudo groupadd --system minio
sudo useradd -s /sbin/nologin --system -g minio minio
sudo usermod -a -G minio,staff minio
```

We need to give ownership of the minio working directory and access to the binary, so we can update it later on:

```bash
sudo chown -R minio:minio /data/
sudo chown minio:minio /usr/local/bin/minio
```

Grant it additional networking permissions:

```bash
sudo setcap cap_net_bind_service=+ep /usr/local/bin/minio
```

## Configuration
Now we configure a service for starting minio using [Systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md), writing the following lines into /etc/systemd/system/minio.service. Make sure to set the right working directory.

```basH
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

```BASH
# Volume to be used for Minio server.
MINIO_VOLUMES="/data"
# Use if you want to run Minio on a custom port
MINIO_OPTS="--certs-dir /data/.minio/certs --address :443 --console-port :13380"
# Access Key of the server. Older versions used MINIO_ACCESS_KEY instead
MINIO_ROOT_USER= <someAccessKey>
# Secret key of the server. Older versions used MINIO_SECRET_KEY instead
MINIO_ROOT_PASSWORD= <someSecretKey>
# Server Domain, don't use a wildcard here or virtual style paths won't work!
MINIO_DOMAIN= <domain>
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

If you want to have minio starting at system startup:

```bash
sudo systemctl enable minio
```

## TLS encryption and lets encrypt
You should enable TLS by placing a private key, a certificate and eventually a CA certificate into the path supplied by the -certs-dir parameter. In my example it would be /data/.minio/certs. You can read more about securing minio with certificates under [this link](https://min.io/docs/minio/linux/operations/network-encryption.html).

I've started with the creation of a wildcard certificate created by my own trusted CA. However, you could create the same result by using Lets Encrypt. It's important to use a wildcard certificate, as this is a requirement for using [minio as backup target with Hyper Backup](https://itrandomness.com/2020/05/local-backups-with-synology-hyper-backup-and-minio/). We'll run minio in [virtual-host-style requests](https://docs.min.io/docs/minio-server-configuration-guide.html). That's also the reason why you'll need to define the MINIO_DOMAIN variable.

Instead of adding the bucket name to the server domain, the bucket name will be put in front of the server domain. So you'll end up with domains like bucket.domain instead of domain/bucket. This is the reason why you'll need a wildcard certificate for the given domain.

As I'm using all-inkl as hosting provider, I was keen to know if I could use Let's Encrypt wildcard certificates in combination with the DDNS solution offered. However, for using Let's encrypt certificates, you'll need access to your domains DNS records and need to have a way to update TXT records, as the certs will automatically expire after 90 days. The general setup in combination with all-inkl is explained [here](https://stevenschwenke.de/GeneratingTLSCertificatesUsingCertbotManualModeAndDNSChallengeAndSetupWithAllInkl).

This was also the place, where I found [kasserver](https://github.com/fetzerch/kasserver). kasserver provides an interface to the adminstration interface of all-inkl. It's especially useful for setting up Let's encrypt certs using [certbot](https://github.com/fetzerch/kasserver#kasserver-dns-certbot).

### Install pip and venv
I had to reinstall the raspberry pi and had to do a few preparations before kasserver could be installed. The python was installed via APT, so it was [managed externally](https://stackoverflow.com/a/75696359/831825). This caused some troubles for me and I had to create a dedicated environment, that is available as [system-site-package](https://stackoverflow.com/a/76672519/831825):

```bash
sudo apt install python3.11-venv
python3 -m venv ~/.local --system-site-packages
```

The python packages that are now installed are put into the venv in `~/.local`. Its `bin` folder is normally part of the PATH environment variable, so every command installed here will be available after you log again to a new shell.

### Install kasserver

Install it with

```bash
~/.local/bin/pip install kasserver
sudo apt-get install libxslt-dev
```

Setup the KAS credentials in ~/.netrc

```bash
machine kasapi.kasserver.com
login USERNAME
password PASSWORD
```

Restrict access to the file to only your user

```bash
chmod 600 ~/.netrc
```

Test the installation with

```bash
kasserver-dns list your.domain
```

### Install certbot

```bash
sudo apt-get install certbot
```

Setup a user and folder for certbot

```bash
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

Request a certificate that is valid as wildcard cert and also for the top domain:

```bash
certbot certonly -d *.subdomain.domain.com --config-dir /home/pi/letsencrypt/config --work-dir /home/pi/letsencrypt/work --logs-dir /home/pi/letsencrypt/logs --preferred-challenges dns --manual --manual-auth-hook /home/pi/.local/bin/kasserver-dns-certbot --manual-cleanup-hook /home/pi/.local/bin/kasserver-dns-certbot -m your@email.domain
```

## Setup NTFS formatted USB drive
I've got an NTFS formatted USB drive attached to the pi. It's my backup storage. I've selected NTFS since it can be read by macOS without problems. For ext4 I'll need to use FUSE or Paragon extFS, which I don't want to buy.

The setup for the NTFS drive is explained in [good detail here](https://gist.github.com/etes/aa76a6e9c80579872e5f).

Make sure that you'll add the user that mounts the NTFS drive is also part of the minio group, e.g. `sudo usermod -a -G minio,staff,usergroup minio`. I've even tried to mount the complete drive as minio:minio using this entry in `/etc/fstab` to avoid permissions problems:

```bash
UUID=4EE12D1B5321171F /mnt/backups ntfs-3g      auto,exec,rw,uid=995,gid=991    0       2
```

The ID of the minio user can be found using 

```bash
id minio
uid=995(minio) gid=991(minio) Gruppen=991(minio),50(staff)
```

However, as we can see later on, I've changed this back to the ID of my raspberry pi user, e.g. `pi`.

## Restart and testing

You can start minio using:

```bash
sudo systemctl start minio
```

Read the entire log:
```bash
journalctl -u minio
```

Once it is started, you can reach it via https://[serverip|localhost]:9000. You can login to the web interface using the two keys defined in the /etc/default/minio file.

Create a new bucket. You'll use this bucket as your backup target in Hyper Backup.

The setup of Hyper Backup with S3 compatible providers is explained [here](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Backup/How_to_back_up_your_data_to_cloud_services_with_Hyper_Backup).

## Import of existing data

When you've already got data on your machine and want to add it to an Bucket, you'll need to use the `mc` tool. First, you'll have to setup an alias:

```bash
mc alias set destminio https://localhost minioadminuser minioadminpassword
```

Now you can test this locally. Since you're connecting to localhost, you'll have to disable the certificate check as well.

```bash
mc admin info destminio --insecure
```

[Import the data](https://blog.min.io/data-migration-tools-into-minio/) from the local filesystem:

```bash
mc mirror /volume/old-data destminio/yourBucketName --insecure
```

Be aware, this is a very slow operation (around 5MB/s on a Raspberry Pi 3b).

## Run as docker container
I've had some troubles with the setup of minio so I've tried to use it via docker. 

### Install docker
There's a really good [documentation](https://docs.docker.com/engine/install/raspberry-pi-os/#install-using-the-repository) for installing the official docker packages and not the ones provided by Rasbpian. Quite nice and worked out of the box.

### Minio in docker
On my raspberry Pi 3b, I required an arvm7 compatible image. The official docker image doesn't provide this so I've selected this one instead: `tobi312/minio:latest`

I've setup my `docker-compose.yml` like this:

```yaml
version: '2'
services:
    minio:
      container_name: minio
      command: ["server", "--certs-dir", "/certs", "--address", ":443", "--console-address", ":9001", "/data"]
      environment:
        - MINIO_ROOT_USER=foo
        - MINIO_ROOT_PASSWORD=bar
        - MINIO_DOMAIN=buckets.domain.com
      image: tobi312/minio:latest
      user: 1000:1000
      ports:
        - '443:443'
        - '9001:9001' 
      volumes:
        - /home/pi/letsencrytp/config/live/buckets.domain.com/privkey.pem:/certs/private.key
        - /home/pi/letsencrytp/config/live/buckets.domain.com/cert.pem:/certs/public.crt
        - /home/pi/letsencrytp/config/live/buckets.domain.com/chain.pem:/certs/CAs/chain.pem
        - /mnt/backups/minio:/data
      healthcheck:
        test: ["CMD", "curl", "-fail", "http://localhost:443/minio/health/live"]
        interval: 60s 
        timeout: 10s 
        retries: 3
      restart: unless-stopped
```

Whereby `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` are the same as before the Access and Secret Key. Make sure that you'll set `MINIO_DOMAIN` without wildcards. The ID should be the same ID as of the user that owns the letsencrypt certificate files as well as the mounted data directory.

Start the compose file with `docker compose up -d` when you're next to the `docker-compose.yml` file.

## Reconnect S3 Hyperbackup
If you change your domain or S3 provider, you'll have to reconnect an existing Hyperbackup key with a new S3 destination. Create a new S3 backup, select S3 as destination and choose a custom configuration. Use the credentials you've used before, including the new URL. Hyperbackup tries to connect automatically to the S3 server and lets you select the bucket and eventually any existing folders in that bucket. I've selected here the folder where I've imported my existing Hyperbackup.

Hyperbackup asks for a schedule and which folders to backup. I've selected none, but when askes for the encryption key or password of the backup, you'll can connect an existing backup with the new location. Hyperbackup will download Meta information about the backup, which takes some time, depending on your connectivity and the connectivity of your S3 server. It then shows that it is reassociating the backup, so I assume it will show later up with all its contents and settings which were backed up. I'll update this post accordingly, when I know more.