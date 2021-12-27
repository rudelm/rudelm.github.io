---
author: Centurio
categories:
- Apple
- Linux
date: "2015-04-14T18:33:41Z"
guid: http://centurio.net/?p=2230
id: 2230
tags:
- Hyperion
- KODI
- XBMC
title: Forward Kodi/XBMC video information to hyperion on Raspberry Pi
url: /2015/04/14/forward-kodixbmc-video-information-to-hyperion-on-raspberry-pi/
---
My current network setup allows me only to use small bandwidth connections between the living room (that&#8217;s where my Raspberry Pi is used as my Mediacenter) and office (my NAS). However, my Macbook is fast enough and can access the NAS wirelessly, so that I often use it as a replacement for the hardwired Raspberry Pi.

However, I cannot use my Hyperion Ambilight setup behind the TV in combination with the Macbook, because its only connected to the Raspberry Pi. But yesterday I&#8217;ve found [this plugin](https://github.com/tvdzwan/hyperion/wiki/XBMC-addon-%28not-for-RPi%29) which enables the Kodi setup on my Macbook to connect to the Hyperion Server on my Raspberry Pi over network.

  1. Download the zip file with the content of the git repository.
  2. Start Kodi on the Macbook and install it using the add on manager. You can point to the zip file directly without the need to unzip it first.
  3. Configure the installed plugin to connect to the ip of your Hyperion server.
  4. Start a video and be amazed that the lights on your TV will work wirelessly 😉