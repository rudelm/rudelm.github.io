---
author: Centurio
categories:
- Apple
- Hardware
- Linux
- Raspberry Pi
date: "2018-03-08T19:52:37Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=3159
id: 3159
tags:
- HomeBridge
- HomeKit
title: DIY HomeKit with Raspberry Pi and Xiaomi Robot Vacuum
url: /2018/03/08/diy-homekit-with-raspberry-pi-and-xiaomi-robot-vacuum/
---
Inspired by tweets of [Steven Troughten-Smith](https://twitter.com/stroughtonsmith), people started to experiment with Raspberry Pi's as DIY HomeBridge devices. One of them is [Wojtek Pietrusiewicz](https://twitter.com/morid1n). He wrote a [nice article](https://infinitediaries.net/using-a-raspberry-pi-zero-w-to-add-a-camera-and-a-xiaomi-air-purifier-2-to-homekit-via-homebridge/) which I used as base for this post.

# Introduction

I own a Xiaomi Robot Vacuum. This robot can be controlled by the Xiaomi app, however, I don't like it very much. The idea is to control this robot over HomeKit. To use HomeKit, I use an old Raspberry Pi 1B. The software will be [HomeBridge](https://github.com/nfarina/homebridge).

# Setting up the Pi

## Installation and Configuration of Raspbian

  * Download [Raspbian lite image](https://www.raspberrypi.org/software)
  * Download [Etcher](https://etcher.io/)

Use Etcher to write the image to the SD card. Remount that SD card and add a file called &#8222;ssh" in the root of the mounted partition. This will enable SSH from the beginning so that you can login directly to the Pi. I don't want to attach a screen or keyboard to that machine so it will only be reachable over the network. Now boot your Pi from this SD card.

Identify the Pi's IP (e.g. by looking at the network overview in your router). Now connect to that IP with user &#8222;pi". The default password is &#8222;raspberry". Please change the password now with `passwd` and assign a new user password.

Update everything with apt:

<pre class="lang:default decode:true">sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get clean
sudo reboot
```

 

## Install nodejs 8.9.4

According to Wojtek only this version works currently with HomeBridge. I did not test any other version so I'm just describing what I did on my machine:

  1. Download nodejs for the PI into your users homefolder, e.g. with `wget https://nodejs.org/dist/v8.9.4/node-v8.9.4-linux-armv6l.tar.xz`
  2. Unpack the file with `tar -xvf node-v8.9.4-linux-armv6l.tar.xz`
  3. `cd node-v8.9.4-linux-armv61`
  4. `sudo cp -R * /usr/local/`
  5. add `export PATH=$PATH:/usr/local/bin` to e.g. `~/.bashrc`
  6. node should be now available

## Install HomeBridge

  1. Install the necessary libraries: `sudo apt-get install libavahi-compat-libdnssd-dev`
  2. Install HomeBridge with npm: `sudo npm install -g --unsafe-perm homebridge`
  3. open `/etc/default/homebridge` and safe it with this content: <pre class="lang:default decode:true"># Defaults / Configuration options for homebridge
# The following settings tells homebridge where to find the config.json file and where to persist the data (i.e. pairing and others)
HOMEBRIDGE_OPTS=-U /var/homebridge
 
# If you uncomment the following line, homebridge will log more 
# You can display this via systemd's journalctl: journalctl -f -u homebridge
# DEBUG=*
```

  4. open `/etc/systemd/system/homebridge.service` and safe it with this content: ```
[Unit]
Description=Node.js HomeKit Server 
After=syslog.target network-online.target
 
[Service]
Type=simple
User=homebridge
EnvironmentFile=/etc/default/homebridge
ExecStart=/usr/local/bin/homebridge $HOMEBRIDGE_OPTS
Restart=on-failure
RestartSec=10
KillMode=process
 
[Install]
WantedBy=multi-user.target
```

  5. <pre class="lang:default decode:true">sudo useradd --system homebridge
sudo mkdir /var/homebridge
cp /usr/local/lib/node_modules/homebridge/config-sample.json ~/.homebridge/config.json
```

## Setting up HomeBridge with Xiaomi Robot Vacuum

  1. `sudo npm install -g homebridge-xiaomi-mi-robot-vacuum miio`
  2. open `~/.homebridge/config.json` and safe it with this content: <pre class="lang:default decode:true">{
 "bridge": {
 "name": "Homebridge",
 "username": "XX:XX:XX:XX:XX:XX",
 "port": 51826,
 "pin": "031-45-154"
 },
 
 "description": "HomePi Homebridge.",
 
 "accessories": [
 {
 "accessory": "MiRobotVacuum",
 "name": "Vacuum Cleaner",
 "ip": "IP_ADDRESS_OF_THE_ROBOT",
 "token": "TOKEN_RECOVERED_FROM_APP",
 "pause": true
 }
 ]
}
```
    
    Generate a new MAC address separated by : using [this website](https://www.miniwebtool.com/mac-address-generator/). You'll need the IP address of your Xiaomi robot as well as the token. There are [several ways to get the token](https://github.com/jghaanstra/com.xiaomi-miio/blob/master/docs/obtain_token.md). I've extracted mine from the iOS backup. Instead of uploading the token I've used this command on the token taken from the sqlite database:
    
    <pre class="lang:default decode:true">echo '0: &lt;YOUR HEXADECIMAL STRING&gt;' | xxd -r -p | openssl enc -d -aes-128-ecb -nopad -nosalt -K 00000000000000000000000000000000

```

  3. Check if everything is working by starting homebridge for the first time. It should show a QR code. If it does, cancel the process with ctrl+c

## Automate HomeBridge startup

```
cp ~/.homebridge/config.json /var/homebridge
sudo cp -r ~/.homebridge/persist /var/homebridge
sudo chmod -R 0777 /var/homebridge
sudo systemctl daemon-reload
sudo systemctl enable homebridge
sudo systemctl start homebridge
sudo systemctl status homebridge
```

# Adding the HomeBridge to iOS devices

  1. Install the Home app, if you've removed it from your device. You can reinstall it from the App store.
  2. Open the Home app and add a new device
  3. If you've give the app access to your camera, you can scan the QR code you've seen earlier. However, HomeBridge is now running as a daemon in the background so you won't see that QR code. You can add the bridge manually by using the PIN you've set in the config.