---
author: Centurio
categories:
- Home Automation
- Linux
- Raspberry Pi
date: "2021-09-16T20:47:53Z"
guid: https://centurio.net/?p=3470
id: 3470
tags:
- Homematic
title: Howto disable Raspberry Pi Status LEDs with RaspberryMatic
url: /2021/09/16/howto-disable-raspberry-pi-status-leds-with-raspberrymatic/
---
I&#8217;m using a RaspberryPi 3 with RaspberryMatic distribution to control my HomeMatic thermostats. This distribution has a &#8222;heartbeat&#8220; functionality, which leds the green LED of the Pi light up in constant time intervals.

These LEDs are quite strong and disturb the sleep of my family. Therefore its time to [disable these leds](https://homematic-forum.de/forum/viewtopic.php?t=47186#p473755).

Connect via SSH to the RaspberryMatic installation. Edit or create the file /usr/local/etc/rc.local and add this content:

<pre class="wp-block-code"><code>#!/bin/sh
echo none >/sys/class/leds/led0/trigger
echo none >/sys/class/leds/led1/trigger</code></pre>

Now make this script executeable:

<pre class="wp-block-code"><code>chmod +x /usr/local/etc/rc.local</code></pre>

This script is executed on each start and disables the LEDs completely. No need to use some duct tape to mask the LEDs anymore 🙂