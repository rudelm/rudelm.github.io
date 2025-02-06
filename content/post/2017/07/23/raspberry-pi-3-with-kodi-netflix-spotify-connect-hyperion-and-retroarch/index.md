---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2017-07-23T09:08:27Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=2347
id: 2347
image: /2017/07/23/raspberry-pi-3-with-kodi-netflix-spotify-connect-hyperion-and-retroarch/images/LibreElecLogo.png
tags:
- basteln
- Emulator
- KODI
- LibreElec
- Netflix
- SNES
- Spotify
title: Raspberry Pi 3 with Kodi, Netflix, Spotify Connect, Hyperion and RetroArch

---
# Introduction
I'm currently using an old Mac Mini from 2009 as my media center. I've updated it recently with more RAM and an SSD but it has its problems with Bluetooth, regardless my used bluetooth card or USB adapter. Before this setup I've used a Raspberry Pi 3 with LibreElec which I've now reactivated successfully.

I'm using the Mac Mini for hearing Spotify, watching Netflix and Sky Go Connect, SNES Emulator with Xbox 360 and PS3 Gamepads and of course Kodi as media center in combination with Hyperion on a Raspberry Pi 1 as Ambilight clone. I've had to replace all this functionality with the Pi 3, but luckily it is possible!

## LibreElec
I've started with [LibreElec](https://libreelec.tv/) (8.0.2 stable) and installed it on the Pi 3. I had to copy the necessary Kodi files for setting the used sources and mysql database, so that I get my existing library and its viewing status.

## Hyperion
Hyperion was [easy to install](https://docs.hyperion-project.org/en/user/Installation.html) via HyperionRemote. I only had to enable guest control for external resources in Kodi, so that Hyperion could properly shut down the backlight while the main menu is being displayed.

## SNES emulator
The SNES emulator can be used on LibreElec using the Kodi add-on [Gamestarter](https://github.com/bite-your-idols/Gamestarter). Just follow the GitHub instructions.

## Xbox360 Gamepads
My Xbox 360 Gamepads where installed without problems. I just had to connect them via the USB adapter and pair them with the adapter. They are usable in Kodi as well as in Gamestarter without further configuration. I think that PS3 gamepads will probably behave similar.

## Bluetooh Mac Keyboard and Trackpad
The Bluetooth Mac Keyboard and Trackpad can also be paired with the Pi 3 via LibreElecs system settings. This allows a better search since you don't need to use the onscreen Keyboard.

## Spotify Connect
For Spotify I've just wanted the Pi 3 to appear as a Spotify connect speaker. The mobile apps and my other machines in the network are a better solution to select the music I want to hear, so I just wanted the Pi 3 to appear as a target. The [Librespot](https://forum.libreelec.tv/thread/8438-librespot-addon/) provides this cool feature and also enables you to add easily Spotify connect to other rooms in your house with just a Raspberry Pi. Just search in the add-on for Librespot and install it. After a restart its active. Spotify connect is available immediately and stops automatically once a movie is started. It will be available again once the movie is really stopped (being paused is insufficient). Connecting to Librespot is really fast and works even better than with my Heos speakers!

{{< img "images/SpotifyConnectPi3.png" "Spotify Connect showing the Pi3" >}}

## Netflix
Netflix is a completely different beast. Netflix is relying on a library called WideVine which handles the DRM. Google created a version for Chrome on ARM devices and some LibreElec and Kodi developers found a great way to integrate all this into the next version of LibreElec 9 and Kodi 18. So you need to update to [LibreElec 9 alpha](https://forum.kodi.tv/showthread.php?tid=298461). Copy the downloaded update file for Raspberry Pi 2 and 3 and put it into the update folder of your Pi 3. Now just restart and you'll get the new version. However, be sure to make a backup of your library, just in case anything doesn't work as expected!

You'll now need the WideVine libs, you can install them with this command on your Pi:

```lang-bash
curl -Ls http://nmacleod.com/public/libreelec/getwidevine.sh | bash
```

You'll now only need the [plugin.video.netflix](https://github.com/asciidisco/plugin.video.netflix) add-on. Once it is started you'll be asked for your Netflix credentials. If you enter everything correctly you'll have all the options of Netflix displayed as nice library entries in Kodi. Really comfortable if you ask me! It even works directly with the Hyperion Ambilight which is a cool feature. I was able to use 720p without problems, 1080p is too much for the Pi 3 to decode only in software.

Now with LibreElec 9 you'll have problems starting RetroArch via Gamestarter. Luckily there's a [version for LibreElec 9](https://github.com/bite-your-idols/Gamestarter/releases) which you can just install and update your existing add-on.

## Conclusion
Congratulations! You've got now a Rasperry Pi 3 with Kodi 19, Hyperion Ambilight, RetroArch Emulator, Xbox 360 Gamepad support and Spotify Connect. Only thing not working is Sky Go Connect Ticket, due to a missing browser and probably DRM related issues. But since I'm just using it for 3 months to see Game Of Thrones I can workaround this with connecting my MacBook to the TV.