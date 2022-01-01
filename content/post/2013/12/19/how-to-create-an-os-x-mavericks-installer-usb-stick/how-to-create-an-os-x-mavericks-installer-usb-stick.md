---
author: Centurio
categories:
- Apple
date: "2013-12-19T13:00:05Z"
guid: http://centurio.net/?p=2110
id: 2110
image: /wp-content/uploads/2013/12/Mavericks_AppStore.png
tags:
- Mac
- Mac OS X
- Mavericks
- USB
title: How to create an OS X Mavericks installer USB stick
url: /2013/12/19/how-to-create-an-os-x-mavericks-installer-usb-stick/
---
<span style="line-height: 1.5em;">So you want to install OS X Mavericks on your older Mac from an USB stick. But the Mavericks installer is just an app which wants to upgrade your running Mac OS X, so you don't have the option to start a fresh installation.</span>

But there is an option available:

## 1. Download OS X Mavericks

Go to the Mac App Store and search for Mavericks or click this direct link. This will bring you directly to the Mac App Store page for Mavericks. You can download the installer, even when you are already on Mavericks:

<a href="http://centurio.net/wp-content/uploads/2013/12/Mavericks\_AppStore.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2111" alt="Mavericks AppStore" src="http://centurio.net/wp-content/uploads/2013/12/Mavericks_AppStore-300x184.png" width="300" height="184" srcset="https://centurio.net/wp-content/uploads/2013/12/Mavericks_AppStore-300x184.png 300w, https://centurio.net/wp-content/uploads/2013/12/Mavericks_AppStore-800x492.png 800w, https://centurio.net/wp-content/uploads/2013/12/Mavericks_AppStore-35x21.png 35w, https://centurio.net/wp-content/uploads/2013/12/Mavericks_AppStore.png 1001w" sizes="(max-width: 300px) 100vw, 300px" /></a>

The download will take its time to complete. If it's finished, go to step 2. Otherwise you can skip the next part, as you have already downloaded the installer.

## 2. Cancel the installation

When the Mavericks installer opens, don't continue it. Close it over the menu or press &#8222;alt+q&#8220; to quit the installer.

## 3. Connect the USB stick and prepare it

Now connect your USB stick. I recommend a stick with at least 16GB space available (like [this from SanDisk](http://www.amazon.de/gp/product/B00422DCB6)). This stick will be formatted, so make a backup of its content or use a dedicated one especially for this sole purpose.

  * Open the &#8222;Disk Utility&#8220; and select your connected USB Stick.
  * Choose Partition and select 1 Partition. Set the name to &#8222;stick&#8220;. This way we can identify it better in step 4. Select &#8222;Mac OS Extended (Journaled)&#8220; and assign the complete space to this partition:  
    <a href="http://centurio.net/wp-content/uploads/2013/12/Partition\_USB\_Stick.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2114" alt="Partition USB Stick" src="http://centurio.net/wp-content/uploads/2013/12/Partition_USB_Stick-300x258.png" width="300" height="258" srcset="https://centurio.net/wp-content/uploads/2013/12/Partition_USB_Stick-300x258.png 300w, https://centurio.net/wp-content/uploads/2013/12/Partition_USB_Stick-35x30.png 35w, https://centurio.net/wp-content/uploads/2013/12/Partition_USB_Stick.png 745w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  * Be sure to select &#8222;Options&#8220;, &#8222;GUID Partition Table&#8220; instead of &#8222;Master Boot Record&#8220;:  
    <a href="http://centurio.net/wp-content/uploads/2013/12/GUID.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2113" alt="GUID" src="http://centurio.net/wp-content/uploads/2013/12/GUID-300x229.png" width="300" height="229" srcset="https://centurio.net/wp-content/uploads/2013/12/GUID-300x229.png 300w, https://centurio.net/wp-content/uploads/2013/12/GUID-35x26.png 35w, https://centurio.net/wp-content/uploads/2013/12/GUID.png 457w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  * Now press &#8222;Apply&#8220; and let the Mac format the stick.

## 4. Create the Mavericks installer

Open the &#8222;Terminal&#8220; application and enter:

[code]  
sudo /Applications/Install\ OS\ X\ Mavericks.app/Contents/Resources/createinstallmedia -volume /Volumes/untitled -applicationpath /Applications/Install\ OS\ X\ Mavericks.app -nointeraction[/code]

Replace the &#8222;/Volumes/untitled&#8220; with the name of the Volume we've created in step 3, e.g. &#8222;/Volumes/stick&#8220;. This command will ask for your Mac administrator password, so enter it and proceed.

Now the installer will create a bootable USB stick. You should see something like this:

[code]  
Erasing Disk: 0%... 10%... 20%... 30%...100%...

Copying installer files to disk...

Copy complete.

Making disk bootable...

Copying boot files...

Copy complete.

Done.  
[/code]

If you look your desktop, you should see a new volume called &#8222;Install OS X Mavericks&#8220;:

<a href="http://centurio.net/wp-content/uploads/2013/12/Install\_OS\_X\_Maverics\_Icon.png" data-rel="lightbox-image-3" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-full wp-image-2115" alt="Install OS X Maverics Icon" src="http://centurio.net/wp-content/uploads/2013/12/Install_OS_X_Maverics_Icon.png" width="130" height="121" srcset="https://centurio.net/wp-content/uploads/2013/12/Install_OS_X_Maverics_Icon.png 130w, https://centurio.net/wp-content/uploads/2013/12/Install_OS_X_Maverics_Icon-35x32.png 35w" sizes="(max-width: 130px) 100vw, 130px" /></a>If you open it, you will see the &#8222;Install OS X Mavericks.app&#8220; which you could now execute to perfom a normal upgrade installation. But you wanted this stick especially for the creation of new clean installation, therefore reboot your mac.

## 5. Boot into the installer

During the startup sound, press the &#8222;alt&#8220; key. This will open up the boot menu selector. You can now select the Volume we've created. It should be a yellow symbol with an USB logo on it.

&nbsp;

Congratulations, you've created a bootable Mac OS X Mavericks installer USB stick, which you could now use to create a fresh installation of Mac OS (or to create a Fusion drive).