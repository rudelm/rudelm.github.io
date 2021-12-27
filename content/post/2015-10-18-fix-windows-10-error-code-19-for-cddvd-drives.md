---
author: Centurio
categories:
- Windows
date: "2015-10-18T16:42:01Z"
guid: http://centurio.net/?p=2252
id: 2252
image: /wp-content/uploads/2015/10/Windows10DVDRW.png
tags:
- Windows 10
title: Fix Windows 10 error code 19 for CD/DVD drives
url: /2015/10/18/fix-windows-10-error-code-19-for-cddvd-drives/
---
I recently tried to convert a CD to MP3 (as part of my [private copy](https://de.wikipedia.org/wiki/Privatkopie) for cds without protection), since my car stereo doesn&#8217;t have any CD drive at all. Therefore I&#8217;ve installed CDEX. CDEX complained about a missing CD drive, which puzzled me since I know that I have a DVDRW drive installed in my desktop PC. Upon further investigation I&#8217;ve seen no drive letter assignment in the explorer or disk management of Windows 10.

A closer look in the device manager showed me a problem with my drive:

<a href="http://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2253" src="http://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW-264x300.png" alt="Windows 10 code 19 dvd drive" width="264" height="300" srcset="https://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW-264x300.png 264w, https://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW.png 400w" sizes="(max-width: 264px) 100vw, 264px" /></a>

I&#8217;ve tweeted this and got some responses from the official Windows support account. While I like this unexpected help and its experience, their advise wasn&#8217;t really helpful 🙁

https://twitter.com/WindowsSupport/status/655438486657441792

I took control and searched the web for the exact error message from the device manager:

> Windows cannot start this hardware device because its configuration information (in the registry) is incomplete or damaged. (Code 19)

* * *

**Beware: Take a backup of your registry before you edit and just follow instructions from the internet! I cannot be held responsible for damage/problems caused to your machine.**

* * *

&nbsp;

I only found instructions for older Windows versions. However, I&#8217;ve tried those instructions on my machine and found a **LowerFilters** entry in my machine&#8217;s registry:

<a href="http://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW\_fix.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2257" src="http://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW_fix-300x238.png" alt="Windows 10 fix for Code 19" width="300" height="238" srcset="https://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW_fix-300x238.png 300w, https://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW_fix-1024x814.png 1024w, https://centurio.net/wp-content/uploads/2015/10/Windows10DVDRW_fix.png 1286w" sizes="(max-width: 300px) 100vw, 300px" /></a>

&nbsp;

I&#8217;ve deleted it from the registry and rebooted. After the reboot my drive was working as expected without the need for any new driver or firmware updates.