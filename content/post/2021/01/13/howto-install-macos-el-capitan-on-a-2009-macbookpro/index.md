---
author: Centurio
categories:
- Apple
date: "2021-01-13T22:00:10Z"
guid: https://centurio.net/?p=3436
id: 3436
tags:
- Mac
- macOS
title: Howto install macOS El Capitan on a 2009 MacbookPro

---
I'm trying to sell a 2009 MacbookPro. It's the model MacbookPro5.5 and Apple supports macOS El Capitan 10.11 as latest available version.

I've wiped all data from the installed SSD and had to boot from an external disk. Now I've got two problems:

  1. I've only got a Mac with Big Sur and Apple Silicon. I cannot use the package installer from the [download provided by Apple](https://support.apple.com/de-de/HT211683) to create the installer App for El Capitan. However, I need access to the installer so that I'm able to use the createinstallmedia command.
  2. The 2009 MacbookPro is already wiped and has only access to the recovery mode. You cannot execute the package installer in Recovery Mode to extract the media.

Luckily I've found this [blog post from Chris Warrick](https://chriswarrick.com/blog/2020/06/03/reinstalling-macos-what-to-try-when-all-else-fails/) who explained how to extract the installer App from the package:

  1. Attach an external Disk which contains the downloaded pkg from Apple. You'll need enough space on that Disk to extract the pkg and it needs to be writeable
  2. Open the Terminal from inside the Recovery Mode
  3. Go to the mounted volume
  4. Extract the package:

```
$ pkgutil --expand InstallMacOSX.pkg elcapitan
$ ls -F elcapitan
Distribution*       InstallMacOSX.pkg/ Resources/
$ cd elcapitan/InstallMacOSX.pkg/
$ tar -xvf Payload
x .
x ./Install OS X El Capitan.app
x ./Install OS X El Capitan.app/Contents
…
```

Now we can try to create the install media from the installer app. Make sure you've attach another disk which can be overwritten by the installer. In this example its named  "MyBlankUSBDrive":

```
# "Install OS X El Capitan.app/Contents/Resources/createinstallmedia" --volume /Volumes/MyBlankUSBDrive --applicationpath "Install OS X El Capitan.app"
Install OS X El Capitan.app does not appear to be a valid OS installer application.
```

The InstallESD.dmg image is missing, which we'll need to add to the right location:

```
$ mkdir "Install OS X El Capitan.app/Contents/SharedSupport"
$ mv InstallESD.dmg "Install OS X El Capitan.app/Contents/SharedSupport"
# "Install OS X El Capitan.app/Contents/Resources/createinstallmedia" --volume /Volumes/MyBlankUSBDrive --applicationpath "Install OS X El Capitan.app"
Ready to start.
To continue we need to erase the disk at /Volumes/MyBlankUSBDrive.
If you wish to continue type (Y) then press return:
```

Now we'll have a valid installation medium which can be used to start the installer from. You can reboot from that disk and should be able to install El Capitan. 

However, I've encountered another annoying issue which caused the installer to fail:

```
    El Capitan Installer cannot be verified
```

Oh great... On to the next commands you can [try from the Terminal inside the Recovery OS](https://apple.stackexchange.com/a/232016/19241):

  1. `installer -pkg /Volumes/Mac\ OS\ X\ Install\ DVD/Packages/OSInstall.mpkg -target /Volumes/"XXX"` where XXX is the name of the disk you're installing to.
  2. Wait for the installation to say it's complete. You will not see any sort of progress display.

Great, you've got El Capitan installed! [Apple had some issues with certificates](https://tidbits.com/2019/10/28/redownload-archived-macos-installers-to-address-expired-certificates/) and people found a way to either use the above commands for installation or you'll have to tinker with your Macs time settings so that the signature is valid again. I would have expected that Apple resigned all installers so I wouldn't have to use these commands at all but doesn't look like they did.