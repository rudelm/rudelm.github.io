---
author: Centurio
categories:
- Apple
date: "2020-11-11T20:40:48Z"
guid: https://centurio.net/?p=3410
id: 3410
tags:
- autofs
- automount
- Catalina
title: automount not working after macOS Catalina updates
url: /2020/11/11/automount-not-working-after-macos-catalina-updates/
---
I've recently upgraded to macOS catalina. My automount mount for music media <a href="https://centurio.net/2020/10/26/fix-broken-automount-mounts-on-macos-catalina/" data-type="URL" data-id="https://centurio.net/2020/10/26/fix-broken-automount-mounts-on-macos-catalina/">was broken</a>. I fixed it and today it is again not working.

The last change I did was to install the supplemental update for 10.15.7 which seems to overwrite the /etc/auto\_master so my /etc/auto\_smb wasn't loaded anymore. Here's my current working content:

```
#
# Automounter master map
#
+auto_master		# Use directory service
#/net			-hosts		-nobrowse,hidefromfinder,nosuid
/home			auto_home	-nobrowse,hidefromfinder
/Network/Servers	-fstab
/-			-static
/-			auto_smb	-nosuid,noowners
```

Don't forget to run

```
sudo automount -vc
```

after it you've changed the file. Your automount should now work again.