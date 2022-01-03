---
author: Centurio
categories:
- NAS
date: "2020-09-09T22:06:28Z"
guid: https://centurio.net/?p=3347
id: 3347
tags:
- All-Inkl.com
- DynDNS
- Synology
title: Use all-inkl.com DDNS with Synology DiskStation
url: /2020/09/09/use-all-inkl-com-ddns-with-synology-diskstation/
---
# Introduction
I've recently upgraded my all-inkl.com webspace to the [PrivatPlus](https://all-inkl.com/webhosting/privatplus/) tariff. As part of this tariff I'm now able to use DDNS running under the Domains I'm able to manage.

## DDNS in KAS
Setting up [DDNS in KAS](https://all-inkl.com/wichtig/anleitungen/kas/tools/ddns-dynamisches-dns/benutzer-anlegen-im-kas_362.html) is explained quite well. However, I did not see instructions on how to use these credentials on a Synology DiskStation OS. Luckily, [somebody else](https://www.ask-sheldon.com/inkl-com-ddns-synology-nas/) did this already.

The important part was, that when you'll need to customize a DDNS provider first before it can be setup in DiskStation settings.

{{< img "images/All-InklDDNSSynologySettings.png" "Synology DDNS Settings for use with All-inkl" >}}

  * Go to Control Panel, External Access and click on Customize
  * Add a new name for the DDNS provider, e.g. All-Inkl.com
  * Use this Query URL (for IPv4): dyndns.kasserver.com/?myip=\_\_MYIP\_\_
  * Now you can add a new DDNS entry
  * Select All-Inkl.com as provider
  * Enter the credentials as required
  * Enter the hostname you want to setup for DDNS
  * Click on  "Test Connection"
  * The state should be  "Normal"
  * Click on  "OK"