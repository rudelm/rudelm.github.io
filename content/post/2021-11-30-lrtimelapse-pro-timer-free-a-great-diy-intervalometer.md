---
author: Centurio
categories:
- Hardware
- Photographie
date: "2021-11-30T22:24:15Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=2340
id: 2340
tags:
- Arduino
- Timelapse
title: LRTimelapse Pro Timer Free - a great DIY intervalometer
url: /2021/11/30/lrtimelapse-pro-timer-free-a-great-diy-intervalometer/
---
# Introduction
This is an old blog post from 07/06/2017 and I've finally moved it from the draft folder to the published folder. In the meantime, Gunther released a successor to this project called [LRTimelapse PRO Timer 3 and 2.5](https://lrtimelapse.com/lrtpt/). Therefore this blog post is just keeping tracks of what I've did to get it running.

I'm building my own DIY intervalometer. An intervalometer is a device which triggers your camera for a defined number of times in given intervals. This allows you to create cool timelapse movies with your camera.

Gunther Wegner is a well known and recognised photographer who programmed the great software called [LRTimelapse](https://gwegner.de/zeitraffer/lrtimelapse/). This software helps with the creation of timelapse movies and is real gem! Gunther made a lot of improvements over the course of the last few years and this year he posted an [article](https://gwegner.de/know-how/lrtimelapse-pro-timer-free/) about the creation of his LRTimelapse Pro Timer Free.

The timer is a little Arduino project and should provide better results than most of the commercial solutions. Its price is quite cheap, its components easy to order. So even when you aren't a professional maker you'll get this project running in a few hours.

## Required parts

Here's what you'll need. I've ordered my parts from Reichelt electronic in Germany and had some of the parts in my collection already:

  * [2,5mm Klinken Einbaubuchse](https://www.reichelt.de/Klinkeneinbaubuchsen/LUM-KLB-13/3/index.html?ACTION=3&LA=446&ARTICLE=116166&GROUPID=7448&artnr=LUM+KLB+13&SEARCH=klinkenbuchse%2B2%252C5)
  * [BC 337-25 :: Transistor NPN TO-92 45V 0,8A 0,625W](https://www.reichelt.de/BC-337-25/3/index.html?ACTION=3&LA=514&ARTICLE=4986)
  * [1/4W 1,0K :: Kohleschichtwiderstand 1/4W, 5%, 1,0 K-Ohm](https://www.reichelt.de/1-4W-5-1-0-k-Ohm-9-1-k-Ohm/1-4W-1-0K/3/index.html?ACTION=3&LA=446&ARTICLE=1315&GROUPID=3065&artnr=1%2F4W+1%2C0K&SEARCH=1kohm%2Bkohle)
  * [Batteriehalter mit Kabelanschluss](http://www.ebay.de/itm/Batteriehalter-4-x-Mignon-AA-Mignonzelle-Anschlusskabel-4706-/291850397062?hash=item43f3a3a586:g:gKwAAOSw65FXtub-)
  * [Kippschalter 10A-125VAC, 1x Ein-Ein](https://www.reichelt.de/Kippschalter/MS-166/3/index.html?ACTION=3&LA=2&ARTICLE=13140&GROUPID=7584&artnr=MS+166&SEARCH=%252A)
  * [Arduino Uno](https://www.reichelt.de/Einplatinen-Microcontroller/ARDUINO-UNO/3/index.html?ACTION=3&LA=446&ARTICLE=119045&GROUPID=6667&artnr=ARDUINO+UNO&SEARCH=arduino%2Buno)
  * [LCD Keypad Shield with 2&#215;16 LCD](https://www.amazon.de/kwmobile-Display-Module-Tasten-Arduino/dp/B01EYW5R5M/ref=sr_1_1?ie=UTF8&qid=1499364500&sr=8-1&keywords=lcd+keypad+shield)

You'll need the [Arduino IDE](https://www.arduino.cc/) to flash the code. The code is also available from [GitHub](https://github.com/gwegner/LRTimelapse-Pro-Timer-Free).

I've started with just attaching the LCD Keypad Shield to the Arduino and loaded the code on the Arduino. My display worked directly, however, I was only able to use the right button. This is due to little manufacturing differences in the voltage divider used for the Keypad. User [Johannes Z provided a small Arduino snippet](https://forum.lrtimelapse.com/Thread-alternative-lcd-keypad-shields?pid=31865#pid31865) which will help to determine the necessary values for your version of the keypad. I've forked Gunthers repo and added Johannes code to my repo to include it in this blog post. If you're interested in my values please checkout my version of LCD\_Keypad\_Reader.cpp. Otherwise here are only the changed values:

<pre class="lang:default decode:true ">Right = 0
Up = 131.0
Down = 308.0
Left = 481.0
Select 723.0</pre>

[Here's Johannes code](https://gist.github.com/rudelm/463c59a218a4c17fdad8228356446f8b).

After I've updated the values for my shield, the buttons where now working. Now onto some hardware and soldering:

I've tried to put the transistor and resistor onto a small board which wouldn't stand out too much, as I don't know yet how much space I will have in my encasing. Complete soldering time was maybe 3 hours, so its a really nice after work project.

## Create a case

As for the encasing I'm waiting for a friend of mine to finish calibration on his 3D printer. If you don't have access to a 3D printer, you can order one from Logodeckel in [two](http://shop.logodeckel.de/produkt/lrtimelapse-pro-timer-gehaeuse-blau/) [different](http://shop.logodeckel.de/produkt/lrtimelapse-pro-timer-gehaeuse-gruen/) color schemes.