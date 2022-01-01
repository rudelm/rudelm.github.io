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
I've recently upgraded my all-inkl.com webspace to the [PrivatPlus](https://all-inkl.com/webhosting/privatplus/) tariff. As part of this tariff I'm now able to use DDNS running under the Domains I'm able to manage.

Setting up [DDNS in KAS](https://all-inkl.com/wichtig/anleitungen/kas/tools/ddns-dynamisches-dns/benutzer-anlegen-im-kas_362.html) is explained quite well. However, I did not see instructions on how to use these credentials on a Synology DiskStation OS. Luckily, [somebody else](https://www.ask-sheldon.com/inkl-com-ddns-synology-nas/) did this already.

The important part was, that when you'll need to customize a DDNS provider first before it can be setup in DiskStation settings.<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="848" src="https://centurio.net/wp-content/uploads/2020/09/All-InklDDNSSynologySettings-1024x848.png" alt="" class="wp-image-3348" srcset="https://centurio.net/wp-content/uploads/2020/09/All-InklDDNSSynologySettings-1024x848.png 1024w, https://centurio.net/wp-content/uploads/2020/09/All-InklDDNSSynologySettings-300x248.png 300w, https://centurio.net/wp-content/uploads/2020/09/All-InklDDNSSynologySettings-768x636.png 768w, https://centurio.net/wp-content/uploads/2020/09/All-InklDDNSSynologySettings.png 1208w" sizes="(max-width: 1024px) 100vw, 1024px" /> </figure> 

  * Go to Control Panel, External Access and click on Customize
  * Add a new name for the DDNS provider, e.g. All-Inkl.com
  * Use this Query URL (for IPv4): dyndns.kasserver.com/?myip=\_\_MYIP\_\_
  * Now you can add a new DDNS entry
  * Select All-Inkl.com as provider
  * Enter the credentials as required
  * Enter the hostname you want to setup for DDNS
  * Click on &#8222;Test Connection"
  * The state should be &#8222;Normal"
  * Click on &#8222;OK"