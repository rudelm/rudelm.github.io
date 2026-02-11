---
author: Centurio
title: "Adding Tasmota Switches to Homebridge"
date: 2023-02-16T17:00:18+01:00
categories:
- Raspberry Pi
- Linux
- Hardware
tags:
- tasmota
- mqtt
---
## Introduction
I want to control my various smarthome devices via a central UI. I like giving Siri commands to switch on lights or to increase the temperature. For this, I'm using [HomeBridge](https://homebridge.io/) in a Docker container. Adding stuff like HomeMatic is relatively easy, but adding Tasmota switches which are controlled via MQTT are a little bit tricky.

## Installation of the plugin
I've decided to use [Homebridge Mqttthing](https://github.com/arachnetech/homebridge-mqttthing#readme). It supports a lot of Tasmota devices and also supports many generic MQTT devices, since topics can be defined for almost everything including javascript transformation of values.
The plugin itself can be installed from the Homebridge UI. Just search for `Homebridge Mqttthing` and install it.

## Configuration of Tasmota devices
My Tasmota device have this MQTT configuration:

{{< img "images/tasmotaMqttConfig.png">}}


Important to mention is the Full Topic `tasmota/%prefix%/%topic%/` which we'll need later on.

## Configuration of a device in the plugin
A single device hash must be added to the Homebridge `config.json`:

```json
{
    "type": "outlet",
    "name": "Spülmaschine",
    "url": "mqtt://192.168.100.11:1883",
    "username": "<aUserName>",
    "password": "<aPassword>",
    "logMqtt": true,
    "topics": {
        "getOnline": {
            "topic": "tasmota/tele/16A-1/LWT",
            "apply": "return message == 'Online' ? 'ON' : 'OFF';"
        },
        "getOn": "tasmota/stat/16A-1/POWER",
        "setOn": "tasmota/cmnd/16A-1/POWER"
    },
    "integerValue": false,
    "onValue": "ON",
    "offValue": "OFF",
    "accessory": "mqttthing",
    "startPub": {
        "tasmota/cmnd/16A-1/POWER": "",
        "tasmota/stat/16A-1/POWER": ""
    }
}
```

This socket is an outlet and tracks the power consumption of our dishwasher. Its checking `tasmota/tele/16A-1/LWT` to see if the device is actually online and sends data to MQTT. The returned values are translated from the presence of the `Online` string to a boolean flag. It should be the same value that is configured under `onValue` and `offValue`.

The variables `getOn` and `setOn` control and verify the current status of the device.

The `startPub` hash is especially interesting. After a Homebridge restart, the software doesn't know about the current status of the outlet. Upon Homebridge start, the plugin will send an empty message to `tasmota/cmnd/16A-1/POWER` which will trigger a status message on `tasmota/stat/16A-1/POWER` which is then used to confirm the initial state, comparing it with the values defined in `onValue` and `offValue`.

## Conclusion
Adding the tasmota devices was quite fun, especially when the current state of the switch is properly readout. After trying several plugins, I liked [Homebridge Mqttthing](https://github.com/arachnetech/homebridge-mqttthing#readme) most. I'm especially glad that I'm able to get the initial state of the devices right after a restart of HomeBridge.