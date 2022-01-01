---
author: Centurio
categories:
- Apple
date: "2016-09-21T13:10:26Z"
guid: http://centurio.net/?p=2307
id: 2307
image: /wp-content/uploads/2016/09/step9-825x510.png
tags:
- Mac OS X
- Sierra
title: Installing Mac OS Sierra (10.12) on a MacbookPro 5,5 (Mid 2009)
url: /2016/09/21/installing-mac-os-sierra-10-12-on-a-macbookpro-55-mid-2009/
---
Mac OS Sierra was [released yesterday](http://www.macworld.co.uk/news/mac-software/macos-sierra-release-date-uk-macos-sierra-new-features-2016-out-today-3630374/). However, our good old MacbookPro 5,5 (Mid 2009) [isn't](http://osxdaily.com/2016/06/14/macos-sierra-compatibility-list/) officially supported anymore. Luckily, there are [people](http://dosdude1.com/sierrapatch.html) who figure out what is necessary to patch the official installation so that it can be installed again 😉

I've backuped the Macbook and gave the given instructions a try. Instead of reinstalling everything I only updated from El Capitan to Sierra. After the first restart, the Macbook shut down, as it didn't found a valid boot partition.

So I rebooted again to the patched installation media and ran the proposed &#8222;macOS Post Install...&#8220;. I've selected my type of Macbook and let it patch. Additionally I've ran the &#8222;Force Cache Rebuild&#8220; command and rebooted.

The Macbook booted to Sierra 🙂 However, the FaceTime camera wasn't detected and I wasn't able to get it working again. Since there was a &#8222;Legacy USB Support injector&#8220; I think this might cause the problem. The FaceTime camera is connected internally over USB so it seems to have some problems.

I don't think this is a big problem. You'll probably get this somehow fixed with a little time and patience. However, since I'm running a real Mac hardware (and no Hackintosh), I don't want to fiddle around with such basic hardware problems.

**Therefore I can only recommend you to leave your Macbook on El Capitan (10.11) as the largest supported OS.** Seems that Apple wants to get rid of devices older than 7 years, even if they are still doing great (with a SSD and 8GB RAM).