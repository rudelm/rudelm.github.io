---
author: Centurio
title: "Upgrade Mac Mini M4 SSD"
date: 2025-07-06T23:38:23+02:00
categories:
- macOS
tags:
- ssd
- hardware
---
# Introduction

I've had the chance to upgrade a Mac Mini M4 from a 256GB SSD to a 2TB aftermarket SSD. This procedure is already well documented, but I ran into a thing I've wanted to write down.

# Instructions matter

The SSD I installed was ordered from [https://expandmacmini.com/](https://expandmacmini.com/). While the product itself was nice, I've expected some better documentation. It felt like the website is offering only some basic knowledge.

## Hardware installation

The best instructions on how to open the Mac Mini were of course provided by [iFixit](https://de.ifixit.com/Anleitung/Mac++mini+(2024)+SSD+Austausch/180199). However, I did a few things differently.

* used the provided screw driver - Looks like Apple changed again the Torx screws to a more modern version, so I've decided to use the tools provided by the SSD manufacturer
* keep the power button connected - You can do this if you avoid too much pull on the cable by lying it next to the case
* keep the fan connected - It's not necessary to disconnect when you don't pull the cable too much

## Recovery process

My MacbookPro constantly asked for permissions to access the connected Mini when it was connected via USB-C. Additionally, I've ran into this error message:

![Apple Configurator error during restore process](AppleConfiguratorMacMiniM4RestoreError.png)

At first I thought my USB-C cable was bad (I used the one provided by Apple for the iPad Mini 7th gen), but this didn't resolved my issue. Since I've had no motivation to unscrew the case again and I'm pretty confident to have the SSD properly screwed and mounted, I've decided to check the available free space of my Mac. During the first phase of the recovery, the image is expanded, doubling the required place for a recovery to at least 30GB (including the downloaded Recovery IPSW file). Once I've had enough space, it was ok to restore and did not complain anymore.

# Conclusion

Always check your available storage before you'll start restoring a mac. The error messages from Apple Configurator aren't helpful at all.