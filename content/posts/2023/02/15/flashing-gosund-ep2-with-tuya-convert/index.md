---
author: Centurio
title: "Flashing Gosund Ep2 With Tuya Convert"
date: 2023-02-15T22:49:11+01:00
categories:
- Raspberry Pi
- Linux
- Hardware
tags:
- tasmota
- mqtt
---
# Introduction
I've already used a few other Tasmota devices and needed two more sockets running Tasmota on it. The power consumption should be readable and Tasmota enables me to use it with MQTT. I've ended up buying some Gosund Ep2 sockets which looks pretty similar to Gosund EP1/EP111 I've used before. However, flashing them isn't that trivial.

# Firmware 1.0.4 to 1.0.6
The sockets come with version 1.0.4 preinstalled. That version cannot be converted using [tuya-convert](https://github.com/ct-Open-Source/tuya-convert), so you'll need to write the Gosund support a nice email with your wishes ;)

```
Hello.
I recently purchased 2 of the Gosund EP2 smart plugs and was told,
that there is a Firmware 1.06 which would allow me to reflash the
Smartplugs OtA.
I'm aware that doing this will result in the loss of any warranty.

My device information are as follows:

EP2-AR
ID: xxxx
MAC: 48:55:19:xx:xx:xx

EP2-AR 2
ID: xxxx
MAC: 48:55:19:xx:xx:xx



Please activate the ability to download the Firmware for these devices.

Kind regards,
```

You can get the ID and MAC from the official Gosund App, after you've registered the sockets in that app. Hold the Power Button until they light up blue blinking and they should should be visible for adding in the app.

After you've wrote the email, it will take about 2 days for the firmware to show up in your app. Now flash 1.0.6 and verify that the sockets are still working in the Gosund App.

# tuya-convert
I ran tuya-convert on a Raspberry Pi3b+. Please follow the instructions on github regarding the prerequisites installation. Make sure that you've got a phone connected to the opened hotspot. Hold the power button again until it blinks blue. The socket should be detected and the script helps you through the process.

Don't try to exchange the supplied tasmota-lite image with a newer version. This doesn't seem to work, so please start with the version provided by tuya-convert and update the socket afterwards.

# Tasmota template
I'm currently using this template:

```json
{"NAME":"Gosund EP2","GPIO":[576,1,320,1,2656,2720,0,0,2624,32,0,224,0,0],"FLAG":0,"BASE":45}
```

I then only had to follow the calibration suggestions:

{{< youtube mJgZyvLobno >}}

# Conclusion
It's still a gamble. Sometimes flashing Tasmota works, sometimes it doesn't. According to some forums it seems to be important to not flash two sockets in a row. Make a pause and reboot the Raspberry Pi in between to have a clean start. Additionally this was the first time I had to calibrate the hardware measurements, as they were a little bit off.