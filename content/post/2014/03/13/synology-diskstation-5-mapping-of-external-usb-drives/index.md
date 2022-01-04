---
author: Centurio
categories:
- NAS
date: "2014-03-13T23:26:24Z"
guid: http://centurio.net/?p=2128
id: 2128
image: /2012/12/22/synology-ds213-raid-1-oder-shr/images/DS213plus.jpg
tags:
- DiskStation
- Synology
- USB
title: Synology DiskStation 5 - Mapping of external USB drives
url: /2014/03/13/synology-diskstation-5-mapping-of-external-usb-drives/
---
# Introduction
The mapping of external USB drives in Synologys Diskstation 5 is a mystery to me. The order of connected drives does not seem to be of interest and keeps being the same even after a reboot. Especially after the latest update to DiskStation 5, my [DiskStation 213+](http://www.amazon.de/gp/product/B008U69DDG) assigned other than usual drive numbers to my external USB drives. This results in broken backup plans and network volumes.

## Solution
A little Google research led me to this forum entry together with a suitable solution:

  * Unmount/Eject all connected external USB drives
  * Disconnect the drives from the DiskStation
  * Connect with telnet/ssh to your DiskStation and edit the file /usr/syno/etc/usbno_guid.map
  * The number gives you the name of the usbshareX mount point, while the guid behind the equal sign identifies your USB drive. The last entries will propably your connected drives as you can access them from their usbshareX mount points.
  * Remove unwanted entries and restore the number to their original position.
  * Reboot the DiskStation.
  * Reconnect your Devices, starting with the drive with the lowest number first.
  * All done.