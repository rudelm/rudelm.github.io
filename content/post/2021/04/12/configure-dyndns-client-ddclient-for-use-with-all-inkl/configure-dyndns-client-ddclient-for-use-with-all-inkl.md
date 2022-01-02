---
author: Centurio
categories:
- Internet und co
- Linux
date: "2021-04-12T20:00:00Z"
guid: https://centurio.net/?p=3453
id: 3453
tags:
- All-Inkl.com
- DynDNS
- Raspbian
title: Configure DynDNS client ddclient for use with all-inkl
url: /2021/04/12/configure-dyndns-client-ddclient-for-use-with-all-inkl/
---
# Introduction
You can try ddclient, if you don't have a Router or NAS, which updates a DynDNS account. I'm using it on Raspbian and all-inkl as hosting service.

## All-inkl account setup
Create a new dyndns account in kas.all-inkl.com. Go to Tools, DDNS Settings and create a new entry. You'll need the information from this page for the configuration of ddclient.

## Installation
On your Raspberry pi:

```
$ sudo apt-get update
$ sudo apt-get install ddclient
```

## Configuration

Select other as DDNS service provider. Use dyndns.kasserver.com/ as update server with dyndns2 as protocol. Configure username and password as provided by all-inkl. Use eth0 as network interface (we'll change this later on) and add your DynDNS Domainname.

```
$ sudo nano /etc/ddclient.conf
```

Change the file accordingly to your needs:

```
# Configuration file for ddclient generated by debconf
#
# /etc/ddclient.conf

protocol=dyndns2
#use=if, if=eth0
use=web
web=checkip.dyndns.org/
web-skip='Current IP Address: '
daemon=900
syslog=yes
pid=/var/run/ddclient.pid
mail-failure='email@domain.com'
server=dyndns.kasserver.com
login='yourlogin'
password='yourpassword'
subdomain.domain.com
```

This config will use checkip.dyndns.org to get your currently used external IP address. If you'll use eth0, it will probably report the internal IP address of your eth0 interface instead.

If it encounters any errors, it will send an failure email to the provided email.

Now reboot the service and you're done

```
$ sudo service ddclient restart
```