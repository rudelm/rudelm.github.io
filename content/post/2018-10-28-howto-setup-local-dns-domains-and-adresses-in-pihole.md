---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2018-10-28T18:36:27Z"
guid: http://centurio.net/?p=3223
id: 3223
tags:
- DNS
- pihole
title: Howto setup local DNS domains and adresses in pihole
url: /2018/10/28/howto-setup-local-dns-domains-and-adresses-in-pihole/
---
If you use the AVM FritzBox you&#8217;ll now about this dreaded DNS suffix &#8222;fritz.box&#8220; which every device will get in your network, if you decide to use the DNS server of the FritzBox. I wanted to have something different which doesn&#8217;t collide with domains on the internet, e.g. &#8222;stuff.local&#8220;. As I already use pihole as adblocker on DNS level I needed a solution to configure it in pihole. The following info is based on [the pihole forum](https://discourse.pi-hole.net/t/howto-using-pi-hole-as-lan-dns-server/533).

Create a file called lan.list in /etc/pihole and fill it with content in the following format:

```
&lt;ip-address> &lt;hostname>.stuff.local &lt;hostname>
```

Create a second dnsmasq config file which references the file we&#8217;ve just created:

```
echo "addn-hosts=/etc/pihole/lan.list" | sudo tee /etc/dnsmasq.d/02-lan.conf
```

Restart the dns services in pihole:

```
sudo pihole restartdns
```

You should now be able to lookup your stuff.local hostnames on your pi with e.g.

```
nslookup box.stuff.local
Server:		127.0.0.1
Address:	127.0.0.1#53

Name:	box.stuff.local
Address: 192.168.100.1
```