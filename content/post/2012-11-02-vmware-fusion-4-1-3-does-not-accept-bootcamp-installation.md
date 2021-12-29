---
author: Centurio
categories:
- Apple
- Windows
date: "2012-11-02T13:54:22Z"
guid: http://centurio.net/?p=1986
id: 1986
image: /wp-content/uploads/2012/11/bootcamp_logo.jpeg
tags:
- BootCamp
- NTFS
- VMWare
title: VMWare Fusion 4.1.3 does not accept Bootcamp installation
url: /2012/11/02/vmware-fusion-4-1-3-does-not-accept-bootcamp-installation/
---
I'm currently switching from Windows 7 to Windows 8 and I wanted to make a clean install. Therefore I completely removed the [Bootcamp](http://www.apple.com/support/bootcamp/) Partition with the Bootcamp assistent of Mac OS X. However, it could not remove the partition. I've decided to delete the partition manually and to recreate the partition.

The Mac OS X disk utility only allows me to create exFAT or FAT partition, because NTFS is not natively supported. I've decided to use ExFAT and deleted my old Windows 7 installation. After installing Windows 8, I wanted to use my Bootcamp installation on Mac OS X. So I started [VMWare 4.1.3](http://www.amazon.de/gp/product/B005LTV8G0) (The latest version is 5, but I'm not willing to buy the upgrade, the old version works fine under Mountain Lion.), removed the old entry for my Windows 7 Bootcamp installation and wanted to create a new one.

But this failed with several error messages, indicating that the Bootcamp disk could not be configured. After a short Google search, I've [found the problem](http://translate.google.de/translate?sl=de&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fvmware-forum.de%2Fviewtopic.php%3Ft%3D20367&act=url) with the exFAT format of the Bootcamp partition: VMWare Fusion only supports NTFS formatted partitions.

&nbsp;

The lessons learned from my experience:

  * If you create the Bootcamp Partition with the Mac OS X assistent, you will get a 32GB large Partition in the correct useable format.
  * If you delete yourself old Bootcamp partitions and want to reinstall, make sure you format the partition with NTFS instead of any other offered formats. Instructions for this can be seen here.
  * If you use Paragon NTFS4Mac or if you use MacFuse, you could preformat the partition with NTFS. But Windows 7 and 8 want to create a small boot partition for themself, so I would not recommend to go this path. Format the partitions from Windows setup.

&nbsp;

**A small update:**

I was not able to use VMWare again with Bootcamp. Therefore I decided to delete the partition with the Bootcamp assistent, which crashed during this operation. I had to enter the recovery mode of Mac OS X and had to recheck and repair the complete HDD and its partition. I've then changed the size of the HFS+ Volume on the HDD back to its original size and created a new Bootcamp partition using the assistent:

<figure id="attachment_1996" aria-describedby="caption-attachment-1996" style="width: 300px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2012/11/createBootcampPartition.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="size-medium wp-image-1996" title="Creation of a  Bootcamp partition on Mac OS X 10.8" src="http://centurio.net/wp-content/uploads/2012/11/createBootcampPartition-300x202.png" alt="Creation of a  Bootcamp partition on Mac OS X 10.8" width="300" height="202" srcset="https://centurio.net/wp-content/uploads/2012/11/createBootcampPartition-300x202.png 300w, https://centurio.net/wp-content/uploads/2012/11/createBootcampPartition.png 782w" sizes="(max-width: 300px) 100vw, 300px" /></a><figcaption id="caption-attachment-1996" class="wp-caption-text">Creation of a Bootcamp partition on Mac OS X 10.8</figcaption></figure>

&nbsp;

**Next Update:**

No good news to report&#8230; Windows was finally recognized correctly by VMWare, but I couldn't add the Bootcamp installlation. The setup wanted me to reboot into Windows and reboot into Mac OS X, because it thought the Bootcamp partition was not cleanly unmounted:

<figure id="attachment_1998" aria-describedby="caption-attachment-1998" style="width: 300px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2012/11/BootcampNotPrepared.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="size-medium wp-image-1998" title="Bootcamp partition is not prepared - VMWare Fusion 4.1.3" src="http://centurio.net/wp-content/uploads/2012/11/BootcampNotPrepared-300x195.png" alt="Bootcamp partition is not prepared - VMWare Fusion 4.1.3" width="300" height="195" srcset="https://centurio.net/wp-content/uploads/2012/11/BootcampNotPrepared-300x195.png 300w, https://centurio.net/wp-content/uploads/2012/11/BootcampNotPrepared.png 434w" sizes="(max-width: 300px) 100vw, 300px" /></a><figcaption id="caption-attachment-1998" class="wp-caption-text">Bootcamp partition is not prepared - VMWare Fusion 4.1.3</figcaption></figure>

&nbsp;

So I decided to try the new [VMWare Fusion 5.0.1](http://www.amazon.de/gp/product/B008VLUE24) version and suddenly my problems were all gone&#8230; It's sad to see, that you always need a newer software version to work correctly. Especially when Windows 8 runs just fine inside a normal VMWare VM, but not when you are using Bootcamp. My guess would be that you could install Windows 7, configure Bootcamp correctly in VMWare Fusion and then upgrade to Windows 8. But this takes awefully long, so I'll stick to the newer Fusion version. You can test it 30 days for free and after that you have to buy it for 44,99Euro 🙁

&nbsp;