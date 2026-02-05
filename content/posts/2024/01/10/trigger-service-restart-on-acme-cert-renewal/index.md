---
author: Centurio
title: "Trigger Service Restart on Acme Cert Renewal"
date: 2024-01-10T21:52:30+01:00
categories:
- Linux
- Raspberry Pi
tags:
- OpenWRT
- linux
---
# Introduction
I'm using Let's Encrypt certificates on my OpenWRT router. Those certificates are managed by the acme.sh script. Today was the first time, that a certificate expired through the course of the evening, resulting in a lot of problems.
With an expired certificate, I was unable to open the OpenWRT luci webpage. AdGuard Home's interface isn't reachable either, and encrypted DNS requests stop working.

# Checking the crontab
I've setup acme.sh to be executed each night at 00:00 using this crontab pattern:

```bash
# Check LetsEncrypt Certificate renewal at midnight
0 0 * * * /etc/init.d/acme start
```

However, I did not see anything regarding the acme execution during the last view days in the system log. You can either check this in luci or via ssh on the machine using `logread -e acme-acmesh`. I'll have to check if this now working in the future or not. Any manual execution of `/etc/init.d/acme start` is properly logged.

# Issues after the manual renewal
## AdGuard Home
So I've started the renewal process by just calling `/etc/init.d/acme start` and I've ended up in [curl validation errors number 60](https://curl.se/libcurl/c/libcurl-errors.html):

> CURLE_PEER_FAILED_VERIFICATION (60)
>
> The remote server's SSL certificate or SSH fingerprint was deemed not OK. This error code has been unified with CURLE_SSL_CACERT since 7.62.0. Its previous value was 51.

Since I'm using the same certificate for my AdGuard Home installation, I've decided to disable AdGuard Home for a short moment, since I saw a huge amount of DNS requests failing due to this expired certificate. It is used for providing encrypted DNS requests in my network, since AdGuard Home was using the old certificate, it failed to properly answer.

Once I've disabled AdGuard Home, the requests for checking the right DNS challenges at my  providers DNS table started to work and the certificate was renewed.

A restart of AdGuard Home helped to reload the renewed certificate. I've ran `/etc/init.d/AdGuardHome reload`.

## Luci / OpenWRT Web Interface
The next page that complained was the Luci web interface of OpenWRT. A restart of the uhttpd service helped: `/etc/init.d/uhttpd reload`

# Automating the restarts
I've searched for ways to automate the restarts of affected services, once the certificate was renewed. Luckily I've found [this GitHub issue](https://github.com/openwrt/packages/issues/15610). It pointed me to [this commit](https://github.com/openwrt/packages/commit/e84f6514538f0638507ce8066f801374db6f4150) which shows how nginx could be restarted using a process called [hotplug](https://openwrt.org/docs/guide-user/base-system/hotplug).

I've created two files in `/etc/hotplug.d/acme`:

`/etc/hotplug.d/acme/00-luci`
```bash
if [ "$ACTION" = renewed ]; then
        /etc/init.d/uhttpd reload
fi
```

`/etc/hotplug.d/acme/01-adguard`
```bash
if [ "$ACTION" = renewed ]; then
        /etc/init.d/AdGuardHome reload
fi
```

These files should be now triggered in case of an acme `renewed` event, so that the services are rebooted.

Don't forget to add these files to your OpenWRT backup file configuration, if you'll intend to include them in backups. Just add `/etc/hotplug.d/acme/` to the list of saved files/folders.

# Conclusion
There's still much to lean when it comes to OpenWRT and its packages. While the certificate renewal process is quite simple, it showed some issues in my configuration which I now hopefully mitigated. We'll see us again in 90 days :)