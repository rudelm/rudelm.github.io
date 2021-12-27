---
author: Centurio
categories:
- Hardware
- Linux
- Raspberry Pi
date: "2016-01-10T18:01:13Z"
guid: http://centurio.net/?p=2280
id: 2280
image: /wp-content/uploads/2016/01/osmc_installer-825x510.png
tags:
- Hyperion
- OpenElec
- OSMC
title: Migrate from OpenElec to OSMC
url: /2016/01/10/migrate-from-openelec-to-osmc/
---
I recently upgraded my ambilight clone from 50 to 104 LEDs and I&#8217;ve also updated my OpenElec installation on my Raspberry Pi B+ to 6.0.0. However, the [hyperiond](https://github.com/tvdzwan/hyperion/wiki/Installation) wasn&#8217;t able to communicate properly with [Kodi](http://kodi.tv/) so that no ambilight information was send to the LEDs: The LEDs would always be black, if I want to watch something on the Raspberry Pi.

<del><a href="https://github.com/tvdzwan/hyperion/issues/440" class="broken_link">I&#8217;ve opened an issue on github</a></del> but I didn&#8217;t get  a useable response so far. The configuration and installation worked fine when I&#8217;ve connected with the iOS app or from the command line.

Today I&#8217;ve tried to use [OSMC](https://osmc.tv/) as surrogate for OpenElec and I&#8217;m really impressed: it worked almost out of the box with my old configuration. So I want to share what&#8217;s necessary to migrate from OpenElec to OSMC:

  1. Create a backup from your OpenElec .kodi folder. You&#8217;ll find this folder on OpenElec in /storage/.kodi
  2. Backup your hyperion.config.json or create a new one with HyperCon according to your setup
  3. Install OSMC on a SD card
  4. Boot from this SD card and follow the initial configuration screen
  5. Connect via SSH to OSMC. default user/password are osmc/osmc.
  6. Install hyperion according to nadnerb&#8217;s [instructions](http://blog.nadnerb.co.uk/?p=182). The spi part is important, since OSMC has SPI disabled by default. You&#8217;ll also want to remove the lirc line since this blocks the pins necessary for the default installation of WS2801 LEDs.
  7. Copy your hyperion.config.json to /etc. Be sure that you&#8217;ve changed the path to your effects folder from /storage/hyperion/effects to /usr/hyperion/effects
  8. Copy your .kodi folder to OSMC&#8217;s /home/osmc folder and overwrite any file
  9. Reboot and enjoy your known settings 🙂