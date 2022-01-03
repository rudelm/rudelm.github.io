---
author: Centurio
categories:
- Windows
date: "2015-07-31T15:21:07Z"
guid: http://centurio.net/?p=2240
id: 2240
tags:
- Update
- Windows 10
title: Update Windows 8.1 Pro to Windows 10 Pro with USB stick
url: /2015/07/31/update-windows-8-1-pro-to-windows-10-pro-with-usb-stick/
---
I'm trying [since last night](http://centurio.net/2015/07/30/update-windows-8-1-pro-to-windows-10-my-experience/) to install the update from Windows 8.1 Pro to Windows 10 Pro on my gaming machine. The experience wasn't smooth as I expected, since I'm using an english Windows installation, while Microsoft's media creation tool always seem to use the german setup of Windows 10.

You cannot upgrade without data loss (your apps are removed), if you install a different language of Windows. The installation of language packs isn't helping here either, so you'll need to install exactly the language version, you've once installed.

<a href="http://centurio.net/wp-content/uploads/2015/07/Windows10NoUpgradeBecauseOfDifferentLangaugeGerman.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2242" src="http://centurio.net/wp-content/uploads/2015/07/Windows10NoUpgradeBecauseOfDifferentLangaugeGerman-300x235.png" alt="Windows 10 No Upgrade possible because of different langauge" width="300" height="235" srcset="https://centurio.net/wp-content/uploads/2015/07/Windows10NoUpgradeBecauseOfDifferentLangaugeGerman-300x235.png 300w, https://centurio.net/wp-content/uploads/2015/07/Windows10NoUpgradeBecauseOfDifferentLangaugeGerman.png 716w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Unfortunately I only know that my Windows version was english (en). English Windows can be either US (en-us) or Great Britain (en-en). So after a few tweets with @verdreaux I've selected en-en and tried to create an USB stick with the Windows 10 update.

https://twitter.com/verdreaux/status/627038983231508481

**Your USB stick needs to be formatted in FAT32 format.** I've started with NTFS but that created an unbootable stick:

https://twitter.com/verdreaux/status/627075414880600064

Ideally you'll use a tool like [Rufus](https://rufus.akeo.ie/), which will create your USB stick from an ISO file, so that you don't have to use the Microsoft tool again. If something fails during the creation, it'll download the 3GB setup files again and again. So its definitely recommended to download the iso in the correct language, architecture and version and then try to write that ISO to a bootable media.

Here's my used rufus setting. I've used MBR but GPT would probably be the better/modern choice:

<a href="http://centurio.net/wp-content/uploads/2015/07/RufusWindows10.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2241" src="http://centurio.net/wp-content/uploads/2015/07/RufusWindows10-216x300.png" alt="Rufus Windows 10" width="216" height="300" srcset="https://centurio.net/wp-content/uploads/2015/07/RufusWindows10-216x300.png 216w, https://centurio.net/wp-content/uploads/2015/07/RufusWindows10.png 409w" sizes="(max-width: 216px) 100vw, 216px" /></a>After the stick creation I've rebooted from the stick. I could now select upgrade. However, the setup suggested to start the upgrade from windows without booting from the installation media.

So I've rebooted and tried the setup again from the USB stick. The setup is finally in english and I hope its working this time. Right now the installation is checking for updates and this takes ages. I'll update this post once I have new results ready.

**Update 15:28:**

The update is running. It seems to keep my installed apps and data:

<a href="http://centurio.net/wp-content/uploads/2015/07/ReadyToInstallAndKeepAppsAndData.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2245" src="http://centurio.net/wp-content/uploads/2015/07/ReadyToInstallAndKeepAppsAndData-300x235.png" alt="Ready to install and keep apps and data" width="300" height="235" srcset="https://centurio.net/wp-content/uploads/2015/07/ReadyToInstallAndKeepAppsAndData-300x235.png 300w, https://centurio.net/wp-content/uploads/2015/07/ReadyToInstallAndKeepAppsAndData.png 716w" sizes="(max-width: 300px) 100vw, 300px" /></a>**Update 19:35:**

It's finally running! All apps & settings are still there and working. Glad that this finally worked out. BTW: Although I installed en-en Windows 10 started with en-us langauge settings.

 