---
author: Centurio
title: "Run Acme.sh Natively on Synology NAS"
date: 2026-02-22T20:50:00+01:00
categories:
- Linux
tags:
- Synology
- Lets Encrypt
---
## Introduction
I've [already written in the past about acme.sh on my Synology NAS](/2023/10/12/configure-lets-encrypt-acme-with-ionos-api-for-synology-dsm/). However, I've recently realized that the `synology_dsm` hook is able to renew certificates, even when 2FA auth is enabled by default. Today I'm writing down what I've did to run acme.sh locally on my NAS.

## Installation
Follow the [official instructions](https://codeberg.org/neilpang/acme.sh/wiki/Synology-NAS-Guide):

```bash
$ sudo su
$ cd ~
$ wget https://github.com/acmesh-official/acme.sh/archive/master.tar.gz
$ tar xvf master.tar.gz
$ cd acme.sh-master/
$ ./acme.sh --install --nocron --home /usr/local/share/acme.sh --accountemail "email@gmailcom"
$ source ~/.profile
```

The regular cron job is disabled by using `--nocron` option. This should be replaced by a scheduled task in the management console.

```bash
/usr/local/share/acme.sh/acme.sh --deploy -d domain -d *.domain --deploy-hook synology_dsm
```

## Configuration
I've reused my existing docker installation and copied the `account.conf` as well as the used `ca` and `domain` certificate folder to `/usr/local/share/acme.sh`. I've then removed everything existing regarding the Synology parameters and placed only `export SYNO_USE_TEMP_ADMIN=1` in the config.

## Moment of truth
Now it's time to test the script. Run the command `` and see how the deploy hook automatically updates the certificate:

```bash
[Sun Feb 22 08:47:51 PM CET 2026] The domain 'domain' seems to already have an ECC cert, let's use it.
[Sun Feb 22 08:47:52 PM CET 2026] Logging into localhost:5000...
[Sun Feb 22 08:47:57 PM CET 2026] Enforcing 2FA-OTP has been disabled to complete temp admin authentication.
[Sun Feb 22 08:47:57 PM CET 2026] Notice: it will be restored soon, if not, you can restore it manually via Control Panel.
[Sun Feb 22 08:47:57 PM CET 2026] previous_otp_enforce_option='admin'
[Sun Feb 22 08:47:59 PM CET 2026] Restored previous enforce 2FA-OTP option.
[Sun Feb 22 08:47:59 PM CET 2026] Getting certificates in Synology DSM...
[Sun Feb 22 08:48:00 PM CET 2026] Generating form POST request...
[Sun Feb 22 08:48:00 PM CET 2026] Upload certificate to the Synology DSM.
[Sun Feb 22 08:48:50 PM CET 2026] Restart HTTP services succeeded.
[Sun Feb 22 08:49:14 PM CET 2026] Success
```

Make sure that you'll disable the docker container, if you've set it up in the past. We don't want it to interfere with the certificate renewals.