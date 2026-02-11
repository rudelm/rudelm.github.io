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
## Introduction
I've moved into a house and wanted to check the temperature and humidity of our rooms. Using HomeMatic thermostats would be very expensive, so I decided to use Aqara Zigbee sensors. Those sensors need a hub or Zigbee USB stick, so they can interact with computers. I've decided to buy a Sonoff Zigbee 3.0 USB Dongle and use it in combination with Zigbee2MQTT docker container on a Raspberry Pi 3b+.

## Installation
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

## Flashing the firmware
Use this docker container to [avoid installing all the dependencies](https://www.zigbee2mqtt.io/guide/adapters/flashing/flashing_via_cc2538-bsl.html) for flashing the firmware. Search for your device while it's connected in `/dev/serial/by-id`. Mine looks like this: `/dev/serial/by-id/usb-Silicon_Labs_Sonoff_Zigbee_3.0_USB_Dongle_Plus_0001-if00-port0`. Previously I would recommend `/dev/ttyUSB0` but that changed in newer Raspbian versions. Also the target device in the docker container should be `/dev/ttyACM0` instead. Get [the link](https://github.com/Koenkk/Z-Stack-firmware/releases) to the latest coordinator firmware from the releases section. Search for `CC1352P2_CC2652P_launchpad_*.zip`. Place that URL as `FIRMWARE_URL` parameter:

```bash
docker run --rm \
    --device /dev/serial/by-id/usb-Silicon_Labs_Sonoff_Zigbee_3.0_USB_Dongle_Plus_0001-if00-port0:/dev/ttyACM0 \
    -e FIRMWARE_URL=https://github.com/Koenkk/Z-Stack-firmware/releases/download/Z-Stack_3.x.0_coordinator_20240710/CC1352P2_CC2652P_launchpad_coordinator_20240710.zip \
    ckware/ti-cc-tool -ewv -p /dev/ttyACM0 --bootloader-sonoff-usb

```

The output should probably look like this:

```bash
Downloading firmware from https://github.com/Koenkk/Z-Stack-firmware/releases/download/Z-Stack_3.x.0_coordinator_20240710/CC1352P2_CC2652P_launchpad_coordinator_20240710.zip
Firmware source: 'CC1352P2_CC2652P_launchpad_coordinator_20240710.zip'
Firmware file:   'CC1352P2_CC2652P_launchpad_coordinator_20240710.hex'
sonoff
Opening port /dev/ttyACM0, baud 500000
Reading data from CC1352P2_CC2652P_launchpad_coordinator_20240710.hex
Firmware file: Intel Hex
Connecting to target...
CC1350 PG2.0 (7x7mm): 352KB Flash, 20KB SRAM, CCFG.BL_CONFIG at 0x00057FD8
Primary IEEE Address: 00:12:4B:00:2A:2E:BC:C4
    Performing mass erase
Erasing all main bank flash sectors
    Erase done
Writing 360448 bytes starting at address 0x00000000
Write 104 bytes at 0x00057F988
    Write done
Verifying by comparing CRC32 calculations.
    Verified (match: 0xd9dd0124)
```

## Using zigbee2mqtt
There are quite a lot of instructions available, so I won't go into details:
* https://www.zigbee2mqtt.io/guide/getting-started/#installation
* https://nerdiy.de/en/howto-zigbee-einen-sonoff-zigbee-3-0-usb-dongle-plus-fuer-zigbee2mqtt-vorbereiten/
* https://www.zigbee2mqtt.io/guide/installation/02_docker.html#running-the-container



## Conclusion
I'm still testing everything but so far I like the stick. The transmission range could be bigger, since I've got now three sensors dropping out. However, this seems to be normal for Zigbee devices. We will see how much this annoys me and if I can find a proper repeater solution that really works.