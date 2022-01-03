---
author: Centurio
categories:
- Apple
date: "2013-12-19T16:31:59Z"
guid: http://centurio.net/?p=2121
id: 2121
image: /wp-content/uploads/2011/05/ssd6.jpg
tags:
- Mac OS X
- Mavericks
- SSD
title: How to create a Fusion Drive on Mac OS X 10.9 Mavericks from scratch
url: /2013/12/19/how-to-create-a-fusion-drive-on-mac-os-x-10-9-mavericks-from-scratch/
---
A few years ago I bought [a SSD kit for my MacbookPro 5.5](http://centurio.net/2011/05/28/macbook-pro-55-mit-intel-320-ssd-und-snow-leopard-migration/). At that time I had decided to use the [Intel SSD 320](http://www.amazon.de/gp/product/B004TBMM0W) separately from my HDD as independent drives. This resulted in increased performance, but I had to decide by myself what I want to place on the faster or larger drive.

With Mac OS X 10.8 Apple introduced the Fusion Drive with the new iMacs. It is based upon the Core Storage Layer of Mac OS and combines a fast SSD with the larger but slower HDD into a logical unit. Mac OS X decides what files it wants to place on the SSD and what on the HDD.

The performance is a little slower compared to my solution with single drives. However, [it is](http://www.anandtech.com/show/6679/a-month-with-apples-fusion-drive/7) [proven fast enough](http://www.macworld.com/article/2017365/lab-tests-pushing-a-fusion-drive-to-its-limits.html), so I've decided to use it under Mavericks. For Mavericks, I've created [a bootable USB stick](http://centurio.net/2013/12/19/how-to-create-an-os-x-mavericks-installer-usb-stick/ "How to create an OS X Mavericks installer USB stick") so that I can start with a fresh installation.

If you want to try it out, this is the way to proceed: First of all, create a bootable backup of your system using [SuperDuper!](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html) or [CarbonCopyCloner](http://www.bombich.com/). Now you should follow the steps from this blog. I'll add my notes and tweaks.

We'll follow option C. But instead of booting from the Recovery Partition, we want to boot from the USB stick which you should've created following my other blog article linked above. This way, we are completely independent of the existing content of either SSD or HDD.

Now delete all content from the SSD and the HDD. Repartition the HDD to use 1 partition. This partition will be used to install a fresh copy of Mavericks. As you've destroyed all partitions on both drives, you don't have a recovery partition on either disk. But the Mavericks installer will create a new recovery partition on the drive on which you've decided to install Mavericks (in this case it's the HDD). This is an important step, as this partition needs to be outside of the logical volume created for the fusion disk. This way you are still able to boot into recovery, in case something goes wrong (you could nevertheless boot from the USB stick, which will allow access to the same recovery tools).

You will now continue with the instructions from the blog and merge the drives to one unit. This unit is now empty and can be used in a new installation run of Mavericks. This way, you've created a bootable Fusion Drive with a fresh installation of Mavericks. It is now your choice, if you want to clone your old installation with one of the cloning tools mentioned before. But you could also start with a fresh copy or you can use the [migration assistent](http://support.apple.com/kb/HT5872).

I've chosen a fresh copy and started from scratch. This is a good start to clean up your Mac from any unwanted old stuff. You've now successfully created a fusion drive on Mavericks. Your Mac will now handle all the logic for you on where to place the files. You may now also activate FileVault 2 to encrypt your Fusion Drive. Beware that the usage of BootCamp requires a separate partition on either SSD or HDD, because Windows will otherwise not boot. If you want this configuration, you may look up the details in [this blog](http://www.saschabuettner.de/wordpress/2013/06/15/fusion-drive-bootcamp-und-die-vorteile-einer-ssd/).