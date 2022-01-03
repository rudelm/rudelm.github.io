---
author: Centurio
categories:
- Apple
- Home Automation
- Raspberry Pi
date: "2021-11-30T22:16:30Z"
guid: http://centurio.net/?p=3239
id: 3239
tags:
- HomeBridge
- HomeKit
title: HomeBridge - Apple HomeKit on Raspberry Pi
url: /2021/11/30/homebridge-apple-homekit-on-raspberry-pi/
---
Two years ago I've started to setup a HomeMatic installation using a Raspberry 3b and a RF module by [ELV](https://www.elv.de/elv-smart-home-zentrale-charly-starter-set-bausatz.html). I can now control the heating and want to control many other connected things as well.

Since I have a lot of Apple devices I want to control my HomeMatic devices with Siri and HomeKit. Fortunately there's a software called HomeBridge which supports a lot of addons which integrate other IoT devices into [HomeBridge](https://github.com/nfarina/homebridge). 

## homebridge

There are quite a few instructions available on the internet so I'll focus on the things I've forgot and/or find useful.

  * <https://blog.braintower.de/homematic-sprachsteuerung-mit-siri/>
  * <https://technikkram.net/2018/07/homematic-homebridge-sprachsteuerung-siri-alexa-anleitung-fuer-raspberry-pi-3b>

## homebridge-homematic

One of these Plugins is called [HomeBridge-HomeMatic](https://github.com/thkl/homebridge-homematic) and integrates HomeMatic devices into HomeBridge.

If you've setup HomeBridge-HomeMatic you'll have a new  "Gewerk" created with name  "Homekit". I've forgot to add new devices I've added to HomeMatic so they never appeared in HomeBridge.

## homebridge-airrohr

You can also track the data from your  "Feinstaubsensor" created by the [luftdaten.info](https://luftdaten.info/en/home-en/) project. It tracks the temperature, humidity and air quality. The plugin's code is [available on github](https://github.com/toto/homebridge-airrohr).

## homebridge-hyperion-light

I've got a hyperion ambilight for my TV. The LEDs can be controlled like a HUE lamp so you can turn them on/off and change the brightness and color. The [homebridge-hyperion-light](https://www.npmjs.com/package/homebridge-hyperion-light) plugin works fine.

## homebridge Xiaomi Robot

There are several plugins which I need to check:

  * https://www.npmjs.com/package/homebridge-xiaomi-roborock-vacuum
  * https://www.npmjs.com/package/homebridge-xiaomi-mi-robot-vacuum
  * https://www.npmjs.com/package/homebridge-mi-robot_vacuum

There are also some good instructions online:

  * https://www.loggn.de/homebridge-xiaomi-mi-robot-vacuum-saugroboter-fehlermeldungen/

## Combination with Apple TV 4K

If you want to use homebridge while you are on the road you'll need to have either an iPad or an Apple TV setup to use the same iCloud account like your phone does. It looks like you'll also need to enable the iCloud Keychain, otherwise the communication won't work and you don't see the homekit setting in your Apple TV settings. However, I've removed iCloud Keychain from my setup and it still seems to be working.