---
author: Centurio
title: "Openwrt Upgrades With SquashFS"
date: 2024-04-04T21:53:02+02:00
categories:
- Linux
- Raspberry Pi
tags:
- OpenWRT
- linux
---
## Introduction
I've recently replaced my Raspberry Pi CM4 eMMC with a CM4 and a microSD card. Reason for this is the annoying update process of OpenWRT in combination with SquashFS. I need a working backup that I can just switch to if the upgrade fails for whatever reasons. So when I updated to 23.05.3 I've used a brand new microSD and flashed it using [Balena Etcher](https://etcher.balena.io/). Everything works fine.

## The problem
My collegue hinted me that I could run into problems when I'm reusing my backup microSD for new installations of OpenWRT running SquashFS. This was something new to me, since so far I've always wrote EXT3/EXT4 images using either `dd` or tools likes Balena Etcher or the [rpi-imager](https://github.com/raspberrypi/rpi-imager). The filesystem will be enlarged to the actual size of the SD card I've got no problems. However, when you'll use SquashFS, some parts of the SD card are used readonly and others are marked as writeable. This is contrast to any other filesystem I used before. My collegue mentioned that this might cause problems where changes to the System settings are not properly stored or storage is getting smaller and smaller over time.

## The solution
The solution is to do a reformat of the SD card using the official [SD Memory Card Formatter](https://www.sdcard.org/downloads/formatter/) of the SD Association. It allows a full overwrite of all existing data on the card so that it behaves like it was a fresh card out of the box.

## Conclusion
I did not verified this yet, but my next update will require me to do a low format of a 64GB microSD, which will probably take quite some time to complete. But if its helping me to avoid problems and strange behaviour afterwards I'll give it a try.