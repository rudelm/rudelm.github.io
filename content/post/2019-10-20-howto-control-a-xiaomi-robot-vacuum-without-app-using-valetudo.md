---
author: Centurio
categories:
- Hardware
- Linux
date: "2019-10-20T11:58:43Z"
guid: http://centurio.net/?p=3290
id: 3290
tags:
- Robot
- Xiaomi
title: Howto control a Xiaomi Robot Vacuum without app using Valetudo
url: /2019/10/20/howto-control-a-xiaomi-robot-vacuum-without-app-using-valetudo/
---
I've [tinkered before](http://centurio.net/2018/03/08/diy-homekit-with-raspberry-pi-and-xiaomi-robot-vacuum/) with my Xiaomi Robot Vacuum but returned to the official Xiaomi app since the existing solutions felt uncomfortable. I even worked on adding Mac support for the [dustcloud](https://github.com/dgiese/dustcloud) software but stopped using the rooted firmware.

A few days ago I've read about [Valetudo](https://github.com/Hypfer/Valetudo). Valetudo is a web interface to the Xiaomi robot being self hosted on the robot. It allows easy extraction of the necessary control token and stops the robot from reporting cleaning and location data to Xiaomi. There's also support for MQTT so that you can integrate it into existing home automation systems.

I followed [the instructions](https://github.com/Hypfer/Valetudo/wiki/Installation-Instructions) on creating a rooted firmware and found a few problems and want to share my solution:

  * The firmware builder creates a firmware package along with SSH keys supplied during the build process. I could not login using those SSH keys and required the SSH key directly from the ~/.ssh folder of the user.
  * Flashing inside a VirtualBox Ubuntu VM doesn't work, even when you use a bridged network interface. You maybe able to request the device token but the flash command always fail.
  * Flashing the robot may fail, if it isn't completely reset to its default. You can reset the robot to factory default by pressing the home and reset button until you hear the chinese voice.
  * You should flash the robot while it is inside its charging station.
  * If you're using a Mac, you can install python3 and the required python packages. This will allow you to flash the firmware directly from your mac.
  * Keep your machine close to the robot during the flashing process, because it might otherwise timeout.
  * Since I'm using a chinese version of the robot, I only hear the chinese voice. In this case you'll need to convert the robot to a european version following [these instructions](https://github.com/dgiese/dustcloud/wiki/Vacuum-Robots-CCC-to-CE-conversion). Once the robot is rebooted you'll hear the english translation and can verify this from the Valetudo interface.

Now you're ready to use Valetudo. I've added a link to the Valetudo homepage on my smartphone. It replaces now the Xiaomi app while it still provides access to the cleaning map, the maintenance hours for replacing parts as well as automated clean up plans. All in all its a really nice piece of software!