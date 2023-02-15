---
author: Centurio
title: "Sonoff Zigbee 3 Usb Stick"
date: 2023-02-15T21:27:47+01:00
categories:
- Raspberry Pi
- Linux
- Hardware
tags:
- zigbee
- mqtt
---
# Introduction
I've moved into a house and wanted to check the temperature and humidity of our rooms. Using HomeMatic thermostats would be very expensive, so I decided to use Aqara Zigbee sensors. Those sensors need a hub or Zigbee USB stick, so they can interact with computers. I've decided to buy a Sonoff Zigbee 3.0 USB Dongle and use it in combination with Zigbee2MQTT docker container on a Raspberry Pi 3b+.

# Installation
Plugin the Zigbee adapter on any of the USB ports of the Raspberry Pi. Now connect with SSH to the Pi. Run `sudo dmesg` and see if you see something like

```bash
usbcore: registered new interface driver ch341
usbserial: USB Serial support registered for ch341-uart
ch341 3-1:1.0: ch341-uart converter detected
usb 3-1: ch341-uart converter now attached to ttyUSB0
```

So the adapter was found as serial device and is available under `ttyUSB0`:

```bash
$ ls -l /dev/ttyUSB0
crw-rw---- 1 root dialout 188, May 16 19:15 /dev/ttyUSB0
```

# Flashing the firmware
Use this docker container to [avoid installing all the dependencies](https://www.zigbee2mqtt.io/guide/adapters/flashing/flashing_via_cc2538-bsl.html) for flashing the firmware. Replace the device with the `ttyUSB` you've seen in `dmesg` output. Its likely `/dev/ttyUSB0` anyways. Get [the link](https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin) to the latest coordinator firmware. Search for `CC1352P2_CC2652P_launchpad_*.zip`. Place that URL as `FIRMWARE_URL` parameter:

```bash
docker run --rm \
    --device /dev/ttyUSB0:/dev/ttyUSB0 \
    -e FIRMWARE_URL=https://github.com/Koenkk/Z-Stack-firmware/blob/master/coordinator/Z-Stack_3.x.0/bin/CC1352P2_CC2652P_launchpad_coordinator_20221226.zip \
    ckware/ti-cc-tool -ewv -p /dev/ttyUSB0 --bootloader-sonoff-usb
```

The output should probably look like this:

```bash
sonoff
Opening port /dev/ttyUSB0, baud 500000
Reading data from ../CC1352P2_CC2652P_launchpad_coordinator_20221226.hex
Your firmware looks like an Intel Hex file
Connecting to target...
CC1350 PG2.0 (7x7mm): 352KB Flash, 20KB SRAM, CCFG.BL_CONFIG at 0x00057FD8
Primary IEEE Address: 00:00:00:00:00:00:00:00
    Performing mass erase
Erasing all main bank flash sectors
    Erase done
Writing 360448 bytes starting at address 0x00000000
Write 104 bytes at 0x00057F988
    Write done
Verifying by comparing CRC32 calculations.
    Verified (match: 0xe0c256fd)
```

# Using zigbee2mqtt
There are quite a lot of instructions available, so I won't go into details:
* https://www.zigbee2mqtt.io/guide/getting-started/#installation
* https://nerdiy.de/en/howto-zigbee-einen-sonoff-zigbee-3-0-usb-dongle-plus-fuer-zigbee2mqtt-vorbereiten/
* https://www.zigbee2mqtt.io/guide/installation/02_docker.html#running-the-container



# Conclusion
I'm still testing everything but so far I like the stick. The transmission range could be bigger, since I've got now three sensors dropping out. However, this seems to be normal for Zigbee devices. We will see how much this annoys me and if I can find a proper repeater solution that really works.