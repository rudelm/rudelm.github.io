---
author: Centurio
categories:
- Hardware
- Linux
date: "2013-09-29T18:06:31Z"
guid: http://centurio.net/?p=2085
id: 2085
image: /2013/09/29/how-to-enable-separated-guest-networks-with-dd-wrt-on-tp-link-tl-wr1043n/ddwrt_controlpanel.png
tags:
- DD-WRT
- router
- TP-Link
- Wlan
title: How to enable separated Guest Networks with DD-WRT on TP-Link TL-WR1043N
url: /2013/09/29/how-to-enable-separated-guest-networks-with-dd-wrt-on-tp-link-tl-wr1043n/
---
# Introduction
I've recently setup a new and shiny [TP-Link TL-WR1043N](http://www.amazon.de/gp/product/B002YETVTQ) Gigabit Router with DD-WRT and wanted to document how I set it up as access point with opening an additional guest network.

## Flashing DD-WRT
First, you need to flash DD-WRT to the Router. As I was using a brand new device, I've chosen the  "factory-to-ddwrt.bin" from the [DD-WRT Router Database](http://www.dd-wrt.com/site/support/router-database). Just type in  "TP-Link TL-WR1043N" and you will see three image files. If you are uncertain, which firmware is the right to choose, try [these](http://www.dd-wrt.com/wiki/index.php/Installation#Choosing_the_Correct_Firmware_-_Extremely_Important) instructions. If you already used DD-WRT, you should know how to make updates to your router. I will not cover this cases in my documentation.

## Enable Wireless Access Point
After flashing, you need to configure it as [Wireless Access Point](http://www.dd-wrt.com/wiki/index.php/Wireless_Access_Point).

When you are ready, open [these](http://www.dd-wrt.com/wiki/index.php/Multiple_WLANs) instructions on how to create  "Multiple WLANs". The TP-Link is Atheros based hardware, which means that all wireless network interfaces will start with  "ath" in their names. Follow the guide, until you come to the part where it describes the  "Command Method for DHCP". Add to the configuration the IP of your local DNS server:

```
# Enables DHCP on br1
interface=br1
# Set the default gateway for br1 clients
dhcp-option=br1,3,192.168.2.1
# Set the DHCP range and default lease time of 24 hours for br1 clients
dhcp-range=br1,192.168.2.100,192.168.2.150,255.255.255.0,24h
dhcp-option=br1,6,[DNS IP 1],[DNS IP 2]
```

Continue with the instructions of the wiki page until you reach the chapter  "Restricting Access". This is the configuration which I used to separate the Guest network from your main network:

```
iptables -t nat -I POSTROUTING -o `get_wanface` -j SNAT --to `nvram get wan_ipaddr`
iptables -I FORWARD -i br1 -m state --state NEW -j ACCEPT
iptables -I FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
iptables -I FORWARD -i br0 -o br1 -m state --state NEW -j DROP
iptables -I FORWARD -i br1 -d `nvram get lan_ipaddr`/`nvram get lan_netmask` -m state --state NEW -j DROP
iptables -t nat -I POSTROUTING -o br0 -j SNAT --to `nvram get lan_ipaddr`
iptables -I INPUT -i br1 -p udp --dport 67 -j ACCEPT
iptables -I INPUT -i br1 -p udp --dport 53 -j ACCEPT
iptables -I INPUT -i br1 -p tcp --dport 53 -j ACCEPT
```

With this configuration I was able to create a separated Guest WLAN.