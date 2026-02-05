---
author: Centurio
categories:
- Hardware
- Windows
date: "2014-07-10T20:04:39Z"
guid: http://centurio.net/?p=2137
id: 2137
tags:
- USB 3.0
- Windows 8.1
title: Windows 8.1 and Intel USB 3.0 eXtensible Host Controller code 10

---
## Introduction
Sometimes my desktop computer does not recognize its attached devices on its USB 3.0 ports. This is especially annoying when you use these ports for your input devices and you are not able to login to your computer.

### Problem
I've ran a few times into this problem, but never found a real working solution to fix this problem. You can still use the USB 2.0 ports for the input devices, so you are able to login again. When you look at your device manager, you will see an yellow exclamation mark on the

**Intel USB 3.0 eXtensible Host Controller**

and if you look at its device details you will see an error code 10. A research on the internet showed me that other people are also affected by this, especially in combination with Windows 8.1 (while Windows 7 and Linux pose no problem).

First of all, there was ~~[this official Microsoft page](http://windows.microsoft.com/en-US/windows-8/install-usb-3-usb-devices)~~ for troubleshooting and installation of USB 3.0 devices. IT gave me no new clues and was therefore useless. Then I was full of joy when I found this page in the MSDN blogs from one of the engineers at Microsoft responsible for the USB 3.0 stack in Windows 8. However, while providing much technical background and tips for debugging, it did not help me with my particular code 10 error. If you search the page for  "code 10" you will also find two people desperately looking for a solution, so I'm not alone with this problem. Another excellent technical resource was [this page](http://janaxelson.com/usb_debug.htm). While providing also a few ideas for what to look for, his ultimate idea was to install the Windows 8.1 update (which I already installed).

So nothing really helped me here. My earlier tries blamed the problem on the integrated USB 3.0 hub of my [Dell U2713HM](http://www.amazon.de/gp/product/B0091ME4A0) monitor, but it would not help to disconnect the hub and power for a clean reboot. I then thought I could find a better driver on the [Asrock page](http://www.asrock.com/mb/Intel/Z77E-ITX/index.de.asp) for my [Z77E-ITX](http://www.amazon.de/gp/product/B007RQ0LQI) board but that did not help either.

### Only solution
Only working solution I came up with was to uninstall the controller and to reboot the computer. After this reboot, the controller was reinstalled and worked again. I honestly don't know what went wrong here, but it is a real annoying thing and I hope that coming Windows updates will fix this.