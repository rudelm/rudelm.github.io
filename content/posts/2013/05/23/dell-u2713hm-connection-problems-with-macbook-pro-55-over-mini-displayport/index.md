---
author: Centurio
categories:
- Apple
- Hardware
date: "2013-05-23T20:40:32Z"
guid: http://centurio.net/?p=2068
id: 2068
tags:
- Dell
- DisplayPort
- DualLink DVI
- DVI
- Mini DIsplayPort
- U2713HM
title: Dell U2713HM connection problems with Macbook Pro 5,5 over Mini DisplayPort

---
## Introduction

After some years with my old [Samsung Syncmaster 205BW](http://www.amazon.de/gp/product/B000F9SNIW), I decided to invest into a new big screen with sufficient possibilities to connect all my computers while avoiding dual or triple monitor setups. After testing several 23 and 24 inch screens, I decided to buy a [Dell U2713HM](http://www.amazon.de/gp/product/B0091ME4A0) from an Amazon Warehouse deals promotion. This screen is really amazing and I cannot live without its WQHD/2560*1440 resolution 🙂

### Using higher resolutions
But to use this high resolution, you must connect it to your computer or mac via [DualLink DVI](http://en.wikipedia.org/wiki/Digital_Visual_Interface#Connector) or [Mini DisplayPort](http://en.wikipedia.org/wiki/Mini_displayport). [HDMI](http://en.wikipedia.org/wiki/HDMI) and [VGA](http://en.wikipedia.org/wiki/VGA) or even normal DVI are only usable up to FullHD/1920*1080. So I could easily use the supplied DualLink DVI Cable to connect my PC (with an Nvidia GTX 660 TI) and my old Macbook Pro 5,5 over its Mini DisplayPort.

While the PC connection is without problems, the DisplayPort tends to forget that there is an external screen attached. The screen will change between black and standard gray/blue from the Mac OS X 10.8. It is not possible to use the external screen until I disconnect and reconnect the Mini DisplayPort cable. Only then, my Mac realizes that there is an external screen and uses it in its native resolution.

### DDC/CI
This problem originates in the [DDC/CI](http://en.wikipedia.org/wiki/Display_Data_Channel) support of this monitor. With DDC/CI it is possible to control your screens settings from your PC/Mac without the use of the screens OSD. While this looks tempting, I would have never used this feature. That is why I decided to deactivate the support in the Dell OSD.

**You can deactivate this option in the settings menu of the Dell screen under the point  "Other settings", then DDC/CI set to disable.**

Suddenly, everything works again and my Mac detects the screen without any problems, even when it wakes up and DisplayPort wasn't selected as source in the monitor.