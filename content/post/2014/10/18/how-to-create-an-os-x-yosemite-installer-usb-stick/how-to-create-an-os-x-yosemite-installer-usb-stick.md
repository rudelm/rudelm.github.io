---
author: Centurio
categories:
- Apple
date: "2014-10-18T21:09:06Z"
guid: http://centurio.net/?p=2150
id: 2150
image: /wp-content/uploads/2014/10/YosemiteAppStoreScreenshot.png
tags:
- USB
- Yosemite
title: How to create an OS X Yosemite installer USB stick
url: /2014/10/18/how-to-create-an-os-x-yosemite-installer-usb-stick/
---
Apple released last Thursday (10-16-2014) Mac OS X 10.10 aka. Yosemite. If you would like to create an OS X installer Boot stick, just [follow the instructions which I already wrote down for Mavericks](http://centurio.net/2013/12/19/how-to-create-an-os-x-mavericks-installer-usb-stick/ "How to create an OS X Mavericks installer USB stick"). Its the same steps. Here are some screenshots, which documented how I reformatted my old Mavericks USB stick for use with Yosemite:

 

<a href="http://centurio.net/wp-content/uploads/2014/10/PartitionStick.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2151" src="http://centurio.net/wp-content/uploads/2014/10/PartitionStick-300x259.png" alt="Partition USB Stick" width="300" height="259" srcset="https://centurio.net/wp-content/uploads/2014/10/PartitionStick-300x259.png 300w, https://centurio.net/wp-content/uploads/2014/10/PartitionStick-1024x886.png 1024w, https://centurio.net/wp-content/uploads/2014/10/PartitionStick-800x692.png 800w, https://centurio.net/wp-content/uploads/2014/10/PartitionStick-35x30.png 35w, https://centurio.net/wp-content/uploads/2014/10/PartitionStick.png 1488w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Now list your disks and see where your USB stick was mounted. Mine is mounted under /Volumes/USBSTICK:

<a href="http://centurio.net/wp-content/uploads/2014/10/DiskUtilList.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2152" src="http://centurio.net/wp-content/uploads/2014/10/DiskUtilList-300x129.png" alt="diskutil list" width="300" height="129" srcset="https://centurio.net/wp-content/uploads/2014/10/DiskUtilList-300x129.png 300w, https://centurio.net/wp-content/uploads/2014/10/DiskUtilList-1024x441.png 1024w, https://centurio.net/wp-content/uploads/2014/10/DiskUtilList-800x344.png 800w, https://centurio.net/wp-content/uploads/2014/10/DiskUtilList-35x15.png 35w, https://centurio.net/wp-content/uploads/2014/10/DiskUtilList.png 1132w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Now you can follow the instructions on how to create the stick with the command line utility inside the Yosemite installer app:

<a href="http://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2154" src="http://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia-300x109.png" alt="Createinstall media Yosemite" width="300" height="109" srcset="https://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia-300x109.png 300w, https://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia-1024x372.png 1024w, https://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia-800x291.png 800w, https://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia-35x12.png 35w, https://centurio.net/wp-content/uploads/2014/10/CreateinstallMedia.png 1132w" sizes="(max-width: 300px) 100vw, 300px" /></a>