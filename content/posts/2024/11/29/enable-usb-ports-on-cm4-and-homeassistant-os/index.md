---
author: Centurio
title: "Enable USB Ports on CM4 and HomeAssistant OS"
date: 2024-11-29T23:07:58+01:00
categories:
- Linux
- Raspberry Pi
- macOS
tags:
- linux
- raspberrypi
---
## Introduction
I've got an unused Raspberry Pi Compute Module 4, that I've tried to flash with HomeAssistant OS. Since it's a Pi with eMMC, I've had to some extra steps to get it writeable for flashing. Once I had it flashed with the OS, I've wanted to configure SSH using the suggested method: take a FAT32 formatted USB stick with your `authorized_keys` file on it and reboot. The OS should configure itself, but never saw my USB stick. A USB SSD showed a power light, but did also not work. So what's the problem?

## Waveshare CM4-IO-BASE-A and it's USB ports
I'm using a [Waveshare CM4-IO-BASE-A](https://www.waveshare.com/wiki/CM4-IO-BASE-A) enclosure and board for the CM4. The wiki explains in a note:

  9: USB2.0 is closed by default, if you need to open it, you need to add dtoverlay=dwc2,dr_mode=host.

Ok, the USB ports are disabled and doesn't work without further configuration. This configuration needs to be done in the `config.txt` that every Raspberry Pi uses to control certain hardware features on startup. This file is normally placed in the boot partition of every installation. On a microSD Card I would have just pulled the card and placed it in a card reader, but I'll have to go a different route.

## Making the eMMC readable on macOS
My CM4 uses a soldered eMMC as memory. To be able to flash it, I'll have to switch the BOOT selection to `ON`. On the Mac, I'll followed [Jeff Geerling's instructions](https://www.jeffgeerling.com/blog/2020/how-flash-raspberry-pi-os-compute-module-4-emmc-usbboot) for flashing an eMMC.

## Making changes to the config.txt
So how I can access the `config.txt` stored in the boot partition of the eMMC? I've started the pi from USB and made its drive readable for the Mac. I've tried `diskutil list` and found a DOS formatted partition on the Pi. This should be the boot partition. This [blog](https://shafi.com.au/electronics/home-assistant-raspberry-pi-cm4-installation-guide/) explains it in more detail. The essential parts are:

```bash
mkdir /user/drive
# Create area to mount FAT partition 
mount -t msdos /dev/disk2s1 /user/drive
```

In `/user/drive` the complete content of the boot partition was readable. Open the `config.txt` and add these parameters in the `all` section, to enable the USB ports:

```bash
[all]
dtoverlay=dwc2,dr_mode=host
```

Save the file, unmount the partition and shut the Pi down. Switch the BOOT selection to `OFF` and reboot with the prepared USB stick.

Home Assistant imports the SSH key and a connection was finally possible.

## Conclusion
Always read the documentation properly. I did not know, that I have to manually enable the USB ports, as a regular sized Pi doesn't need this extra configuration. Now I'm able to use it like a regular one with all its provided ports.
