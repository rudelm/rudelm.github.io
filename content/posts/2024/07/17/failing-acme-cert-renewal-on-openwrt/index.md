---
author: Centurio
title: "Failing Acme Cert Renewal on Openwrt 23.05.03"
date: 2024-07-17T22:32:24+02:00
categories:
- Linux
- Raspberry Pi
tags:
- linux
- OpenWRT
---
# Introduction
My [Uptime-Kuma](https://github.com/louislam/uptime-kuma) notified me about expiring certificates on my OpenWRT router. Since that certificate is also [used by my AdGuard Home installation]({{< ref "/posts/2024/01/10/trigger-service-restart-on-acme-cert-renewal" >}}), I knew trouble was waiting for me just around the corner. Something blocked the cert renewal. Either I'll fix this now or I'll be sitting in a few days without working DNS and insecured OpenWRT ui.

# Analyzing the problem
Acme on OpenWRT isn't run as a regular service. That's why its marked as stopped in the startup selection. It is executed as part of a cronjob/Scheduled Task like this:

```bash
# Check LetsEncrypt Certificate renewal at midnight
0 0 * * * /etc/init.d/acme start
```

I've checked the syslog and found only this error:

```bash
ERROR USER root pid 5285 cmd /etc/init.d/acme start
```

So I've tried to run it manually via SSH by running `/etc/init.d/acme start`, but only got an error around the variable `key_type`. This variable is a new variable, introduced with acme 4.0. However, when I've checked my luci config file in `/etc/config/acme` and it had this configured `option keylength 'ec-384'`. This is the old value and somehow the luci configuration did not have the newest configuration format stored.

# Fixing the problem
I've searched for the error message and found some interesting issues from 2024 regarding acme, lets encrypt and problems with OpenWRT. So I've tried to update everything first to the latest available version, but I'm seeing no other updates:

![Installed software screen from OpenWRT 23.05.03](image.png)

The OpenWRT wiki mentioned an `acme-common` package in version 1.4 from May 2024, which I'm clearly not able to install. The sourcecode for the package [mentions version 1.4](https://github.com/openwrt/packages/blob/master/net/acme-common/Makefile#L11) already, but I'm stuck on `1.0.4`.

The OpenWRT forum had a good [hint](https://forum.openwrt.org/t/letsencrypt-acme-sh-and-luci-app-acme-support-topic/196821/45). In version `1.4.0` [a few lines changed](https://github.com/openwrt/packages/commit/66894032d482625a1a7e22ba4336c6fa5dd35d26) so that any old format config file can be read and translated in the right new format. The only thing I've had to change was [this part](net/acme-common/files/acme.init) in file `/etc/init.d/acme`. If I execute the command now, it will succeed and the certificate is extended.


# Conclusion
There seems to be a new package to be waiting, but it isn't part yet of the stable version. I'll hope this will be fixed soon and I can stop relying on this workaround.