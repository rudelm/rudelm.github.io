---
author: Centurio
categories:
- Windows
date: "2015-10-18T16:42:01Z"
guid: http://centurio.net/?p=2252
id: 2252
image: /2015/10/18/fix-windows-10-error-code-19-for-cddvd-drives/images/Windows10DVDRW.png
tags:
- Windows 10
title: Fix Windows 10 error code 19 for CD/DVD drives

---
## Introduction
I recently tried to convert a CD to MP3 (as part of my [private copy](https://de.wikipedia.org/wiki/Privatkopie) for cds without protection), since my car stereo doesn't have any CD drive at all. Therefore I've installed CDEX. CDEX complained about a missing CD drive, which puzzled me since I know that I have a DVDRW drive installed in my desktop PC. Upon further investigation I've seen no drive letter assignment in the explorer or disk management of Windows 10.

### A Problem
A closer look in the device manager showed me a problem with my drive:

{{< img "images/Windows10DVDRW.png" "Error message in device manager" >}}

I've tweeted this and got some responses from the official Windows support account. While I like this unexpected help and its experience, their advise wasn't really helpful 🙁

https://twitter.com/WindowsSupport/status/655438486657441792

### The Solution
I took control and searched the web for the exact error message from the device manager:

> Windows cannot start this hardware device because its configuration information (in the registry) is incomplete or damaged. (Code 19)

* * *

**Beware: Take a backup of your registry before you edit and just follow instructions from the internet! I cannot be held responsible for damage/problems caused to your machine.**

* * *

 

I only found instructions for older Windows versions. However, I've tried those instructions on my machine and found a **LowerFilters** entry in my machine's registry:

{{< img "images/Windows10DVDRW_fix.png" "The solution in the registry editor" >}}

I've deleted it from the registry and rebooted. After the reboot my drive was working as expected without the need for any new driver or firmware updates.