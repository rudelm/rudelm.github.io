---
author: Centurio
title: "OCLP (OpenCore Legacy Patcher) With Macbookpro11.2"
date: 2023-06-28T20:33:55+02:00
categories:
- Apple
- Hardware
tags:
- OCLP
- macOS
---
# Introduction
I gave my old MacBookPro 11.2 to my parents as a replacement for their old MacBookPro 9.2. Problem with the 11.2 model is, that it doesn't get the latest macOS versions anymore. Therefore I've patched it using the [OpenCore Legacy Patcher (OCLP)](https://github.com/dortania/OpenCore-Legacy-Patcher). The latest macOS versions caused me some troubles and the latest update to macOS 13.4.1 was pretty annoying.

# The Issue
I had OCLP 0.6.5 installed and had also the root patch applied. I've updated to 0.6.7 and installed it to the internal EFI partition and rebooted. Up to this moment everything was still working. I've then decided to use the root patch and that's where the problems started.

## Stuck login
After a restart I was able to login. However, it doesn't progress anymore and the system won't load. 3D acceleration was visible in the progress spinner but that's all.

## Fail safe mode
If you'll hold the `shift` key during the boot process, the mac will boot into a fail safe mode. This ended in a Apple loading screen where the indicator moved only to about the half of the bar and was stuck.

## Verbose mode
If you"ll hold `cmd + v` you'll get the verbose logging during startup. However, this also ended in the same screen as before

# A possible solution
I've searched the OCLP Discord for solutions and hints, but I couldn't find anything helpful. New Github Issues are currently not possible and were also not helpful. After searching a while, I came upon [this post](https://forums.macrumors.com/threads/stuck-on-login-screen-after-opencore-update.2391416/). It was a similar device, only smaller but still the 2014 model. The user describes the same problem as I had them. The working solution was this one:

```
rom another device to rescue your mac.......
Once built - boot from the USB stick and run the ventura installer - it will upgrade your existing ventura install overrating the corrupt files currently stopping you from logging in...
There will be many reboots towards the latter part of the process but this worked for 3 of us (see above) who had tried many things. Expect to take 3-5 hours to do end-to end - the ventura download when making the 0.6.7 usb bootable stick taking much time and Ventura installing taking much time.

Be patient, you can and will get it back - and this method worked for 3 of us.

Your first hurdle is to build a 0.6.7 installer usb stick from another mac - do you have access to another mac ? and when you do - you must select the version of the target machine's version/revision from the config list in the open core builder gui- this is important so you build the right build for the target machine..
```

So I downloaded the OCLP 0.6.7 on my Apple Silicon MBP and created a suitable USB stick with the latest macOS installer. Once I rebooted from the stick, I could select the OCLP patched installer and the machine was working again. Even without any data loss or need for reconfiguration of existing user data.

# Conclusion
Its great that I can still use the old hardware with recent macOS versions. However, the amount of work necessary increases from release to release. My wife's Macbook Air is also patched but is pretty straight forward to update without issues. I guess, sooner or later those machines will need replacement anyways, which is quite sad. Considering that they are still useable for their intended workloads.