---
author: Centurio
categories:
- Apple
date: "2018-05-01T12:43:22Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=3171
id: 3171
tags:
- APFS
- Mac OS X
- SSD
title: How to clean install Mac OS High Sierra without APFS on internal SSD
url: /2018/05/01/how-to-clean-install-mac-os-high-sierra-without-apfs-on-internal-ssd/
---
Did you ever wonder how you can make a clean install on your Mac with High Sierra [without being forced to use APFS](http://osxdaily.com/2017/10/17/how-skip-apfs-macos-high-sierra/)? Well, I just reinstalled my mac using this method and want to explain how I acomplished this:

First of all, you'll need to boot from a Mac OS Version below 10.13 High Sierra. Otherwise you'll get an error message &#8222;Helpertool crashed&#8220;. So in my case I booted from a 10.12 Sierra USB stick.

You can now use the Disk Utility of the recovery OS you currently booted from to clean you complete disk. Format the volume HFS+ journaled and choose a simple name without spaces like &#8222;internal&#8220; (which I used for my internal SSD). Attach the USB stick which contains the High Sierra installer. You can create this installer following [these instructions](https://support.apple.com/en-us/HT201372).

Now exit Disk Utility and open a Terminal. Go to the Volume of your attached High Sierra USB Stick.

cd /Volumes/&#8220;Install macOS High Sierra&#8220;

Start the installation of High Sierra to the freshly formatted HFS+ volume mounted as &#8222;internal&#8220;. This clean installation will also create the Recovery HD partition.

&#8222;Install macOS High Sierra.app&#8220;/Contents/Resources/startOsInstall -agreetolicense -converttoapfs NO -volume /Volumes/internal

More information can be found [here](https://www.tonymacx86.com/threads/guide-avoid-apfs-conversion-on-high-sierra-update-or-fresh-install.232855/). A video of the process and more details are [here](https://derflounder.wordpress.com/2017/09/26/using-the-macos-high-sierra-os-installers-startosinstall-tool-to-avoid-apfs-conversion/). If you execute the startOsInstall command with -usage you'll get a [list of available parameters](https://apple.stackexchange.com/questions/299726/how-to-prevent-conversion-to-apfs-on-high-sierra-install).

&nbsp;