---
author: Centurio
title: "Acme on RaspberryMatic"
date: 2024-11-19T20:08:28+01:00
categories:
- Linux
- Raspberry Pi
tags:
- linux
- acme
---
# Introduction
I'm using a Raspberry Pi 3 with an additional hardware module so it can be used as a HomeMatic home automation server. The software used is called RaspberryMatic and can be integrated in other software like Home Assistant. I'm currently trying to integrate all my IoT devices into Home Assistant and thought it might be a good thing to secure every device as good as possible. In this case I've wanted to use Let's encrypt certificates with my RaspberryMatic installation.

# The problem
RaspberryMatic only supports either the upload of certificates or self signed certificates. Since I want to limit the amount of time spend in this system, I wanted to automate things. A short google search showed me this awesome [GIST](https://gist.github.com/meineerde/6cc3c7ec01e7ebb2aa5be4eecfefeddf) which helped me a lot. We somehow need to add the `acme.sh` script to the RaspberryMatic, so that I'm able to create Let's encrypt certificates. Additionally I want to use DNS validation using the [Porkbun API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi2#dns_porkbun).

# Setup
The GIST recommended to just download the acme.sh script and to use it in standalone mode, which I wanted to avoid by using the Porkbun DNS API. So we'll combine my [previous experience]({{< ref "/post/2023/10/12/configure-lets-encrypt-acme-with-ionos-api-in-openwrt" >}}) with acme and the IONOS DNS API.

## Preparations
Setup a self signed certificate in RaspberryMatic. This is a requirement so that the system is configured to use certificates. Go to Einstellungen -> Systemsteuerung -> Netzwerkeinstellungen and create a self signed certificate following the assistant.

Enable SSH, so that you can connect as root.

## Installation
Once connected with SSH execute these commands:

```bash
mkdir /usr/local/.acme.sh
curl https://raw.githubusercontent.com/Neilpang/acme.sh/master/acme.sh > /usr/local/.acme.sh/acme.sh
chmod +x /usr/local/.acme.sh/acme.sh
```

This is the bare minimum which doesn't install any additional scripts and tools. So run additionally

```bash
/usr/local/.acme.sh/acme.sh --upgrade --home /usr/local/.acme.sh
```

This installs everything else that is required for our project.

Add the automatic renew cronjob by using `crontab -e` and add this line:

```bash
0 0 * * * /usr/local/.acme.sh/acme.sh --cron --home /usr/local/.acme.sh > /dev/null
```

Update 03/25/2025: The entry in the crontab is overriden on each update.

## Setup the DNS API
This step needs only to be done once. [Follow the instructions](https://github.com/acmesh-official/acme.sh/wiki/dnsapi2#dns_porkbun) to export the credentials like this:

```bash
export PORKBUN_API_KEY="..."
export PORKBUN_SECRET_API_KEY="..."
```

# Issue the certificate
The default `acme.sh` uses a different Root CA that requires you to sign up with an email etc. I just wanted a trusted certificate, that is signed by the Let's encrypt CA. First change the default root CA using this command:

```bash
/usr/local/.acme.sh/acme.sh --set-default-ca --server letsencrypt --home /usr/local/.acme.sh
```

Run this command to create the certificate:

```bash
/usr/local/.acme.sh/acme.sh --issue --dns dns_porkbun -d <yourDomainName> --home /usr/local/.acme.sh
--fullchain-file /etc/config/server.crt --key-file /etc/config/server.key --reloadcmd "cat /etc/config/server.key /etc/config/server.crt
 > /etc/config/server.pem && chmod 600 /etc/config/server.pem && /etc/init.d/S50lighttpd reload"
 ```

 # Renew the certificate
 I've executed the same command as the crontab would do:

 ```bash
 /usr/local/.acme.sh/acme.sh --cron --home /usr/local/.acme.sh > /dev/null
 ```

 This will automatically run the `reloadcmd` we've added in the last step, so after a reload you should see the updated certificate already in action.

 # Verify installation
 Open the RaspberryMatic UI and try to change the used protocol from `http` to `https`. You shouldn't get a warning and your new Let's encrypt certificate should be ready to use.

 I've configured my RaspberryMatic to always forward `http` requests to `https` by enabling it in Einstellungen -> Systemsteuerung -> Sicherheit -> Umleitung auf HTTPS aktiv

 Additionally I've setup my Uptime Kuma to monitor the new service so I can see if the certificate renewal is really working.

 # Conclusion
 I'm happy how this worked out. It's quite fast and easy to create self signed certificates. By using the `/usr/local/` location for installation, it should also survive firmware updates. ~~I just hope this will be the case but I'll update the blog post once I know more.~~ Firmware updates require that you'll add the crontab, all other settings survive an update.