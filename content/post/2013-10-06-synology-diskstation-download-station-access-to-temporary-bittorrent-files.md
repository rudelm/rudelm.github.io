---
author: Centurio
categories:
- Hardware
- Linux
- NAS
date: "2013-10-06T03:01:32Z"
guid: http://centurio.net/?p=2088
id: 2088
image: /wp-content/uploads/2012/12/IMG_1291.jpg
tags:
- BitTorrent
- DiskStation
- Synology
title: Synology DiskStation Download Station access to temporary BitTorrent files
url: /2013/10/06/synology-diskstation-download-station-access-to-temporary-bittorrent-files/
---
My [Synology DS-213+](http://www.amazon.de/gp/product/B008U69DDG) can be used as a BitTorrent client. The necessary package &#8222;[Download Station](https://kb.synology.com/en-af/DSM/help/DownloadStation/DownloadStation_desc?version=6)&#8220; is available for free in the standard repositories of the DiskStation. If you use the Download Station for BitTorrent downloads, you may want to access files from the torrent early and before the complete torrent is finished.

In this case you could assume that the setup download folder would be also used as a place for these temporary files. But the Download Station uses a hidden folder for these files. It&#8217;s only visible if you login to your DiskStation using [SSH](http://centurio.net/2012/12/29/synology-ds213-ssh-mit-zertifikaten/) or Telnet. It&#8217;s the folder &#8222;/volume1/@download&#8220;.

If you want to continue to download and want to check the folders content at the same time, you will need to mount this folder to a shared folder which is accessable via SMB or AFP and their likes. The command

`mount --bind /volume1/@download /volume1/your-shared-folder"`

will mount this hidden folder into your-shared-folder. This way you can access all temporary files. But be aware, that this command will only last until you reboot your DiskStation. By the way: I&#8217;m not alone with this wish to access the temporary files. Some people in the official Synology forum also decided to ask for this feature.