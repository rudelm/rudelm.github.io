---
author: Centurio
categories:
- Apple
- NAS
date: "2017-01-13T21:22:27Z"
guid: http://centurio.net/?p=2323
id: 2323
tags:
- Mac OS X
- SMB
title: Slow SMB transfers in Mac OS 10.12.2
url: /2017/01/13/slow-smb-transfers-in-mac-os-10-12-2/
---
I'm using a 802.11ac WLAN to connect to my Synology NAS. With the last Mac OS 10.12.2 update the network performance was catastrophic when I tried to access the NAS via SMB. At first I thought this might have been caused by the WLAN connection but even with a Gigabit LAN connection my transfer rates were around 3-5MB/s.

After a short search online, I've a few hits [describing the actual problem](https://dpron.com/os-x-10-11-5-slow-smb/):

Apple uses their own version of SMB and enabled client signing to mitigate against Man in the middel attacks. Therefore all connections underly this signing process and are way slower.

Therefore I've disabled client-signing on my mac using this command:

```
printf "[default]\nsigning_required=no\n" | sudo tee /etc/nsmb.conf &gt;/dev/null
```

This will write this content

```
[default]
signing_required=no
```

 

to the file /etc/nsmb.conf. After you've set this value you need to unmount all samba shares. If you'll reconnect now, you'll witness a much better performance, starting with faster loading of network shares.

You can revert this change with

<pre class="lang:default decode:true " title="Revert changes made to SMB">sudo rm /etc/nsmb.conf
```

 