---
author: Centurio
categories:
- Apple
date: "2012-09-30T20:47:13Z"
guid: http://centurio.net/?p=1967
id: 1967
image: /wp-content/uploads/2012/09/AppleRemoteAppIcon.png
tags:
- AVM
- Fritz!Box
- itunes
- Remote
- Wlan
title: iTunes 10.7 and Remote 2.4 on iOS 6 - How to reconnect
url: /2012/09/30/itunes-10-7-and-remote-2-4-on-ios-6-how-to-reconnect/
---
I recently tried to use my iPhone 4S with iOS 6 to control my iTunes 10.7 on my Macbook Pro. This used to work but the official Apple Remote App did not successfully connect to iTunes anymore.

I followed the [knowledge base article](http://support.apple.com/kb/TS1741) and tried to reset all remote settings in iTunes, as well as controlling my wireless network settings. After several unsuccessful tries to pair both machines, I tried to switch my Macbook to LAN connectivity instead of WLAN. And this was the first clue, that the problems must have something to do with my network settings, as I could not pair my iPhone with iTunes anymore.

The key to success was to restart my WLAN router ([AVM Fritz!Box 3270](http://www.amazon.de/gp/product/B0019R47PM)). Devices from AVM are [known for their problems](http://translate.google.de/translate?sl=de&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fwww.router-forum.de%2Fboard-avm-fritz%2Fthread-problem-mit-apple-bonjour-ueber-fritz-box-7170-48047-page-1.html&act=url) with Bonjour&#8217;s UDP Multicast packets. They are sometimes blocked when the router is running for too long without reboot. So restarting helped me a lot, because after this I could pair iPhone and iTunes again and could start controlling my Macbook&#8217;s iTunes again 🙂