---
author: Centurio
categories:
- Internet und co
- Linux
- NAS
- Raspberry Pi
- Security
date: "2020-09-26T20:18:33Z"
guid: https://centurio.net/?p=3386
id: 3386
tags:
- OpenVPN
- Raspbian
- WireGuard
title: Setup WireGuard VPN on Raspbian
url: /2020/09/26/setup-wireguard-vpn-on-raspbian/
---
I&#8217;m already using <a href="https://centurio.net/2014/12/23/how-to-use-client-certificates-with-synology-vpn-server-and-openvpn/" data-type="post" data-id="2167">OpenVPN</a> but heard only good things about [WireGuard VPN](https://www.wireguard.com/). For my current project, I need a VPN connection to my home network. I do not want to mess with my currently working OpenVPN setup, so I tried to setup WireGuard VPN on Raspbian.

Start with updating your installed packages. Its [especially important](https://stackoverflow.com/a/62780701/831825) to install the raspberrypi-kernel-headers before the WireGuard installation.:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install raspberrypi-kernel-headers
```

I&#8217;ll use pivpn as setup script. You can install it with curl piping the script to bash like this:

```
curl -L https://install.pivpn.io | bash
```

However, if you don&#8217;t trust that source and doesn&#8217;t want to execute it unseen, you can also [check the script content first](https://install.pivpn.io/) or download the script separately to your machine first.

I&#8217;ve followed now the installation steps which are already pretty good explained by others:

  * <https://pimylifeup.com/raspberry-pi-wireguard/>
  * 

What&#8217;s nice about this script is, that it will also detect installations of pi-hole running on the same machine.

I&#8217;ve used the script to setup WireGuard (as it also supports OpenVPN). I&#8217;ve selected the default port 51820 and created a port forwarding rule in my FritzBox router. After the installation completed, you&#8217;re asked to do a reboot.

Now we&#8217;ll create a new WireGuard profile using

```
sudo pivpn add
```

The script just asks for a profile name and will place the generated profiles in the users home under the config folder.

Setup on the client machine is similar. But instead of using the script for installation, we&#8217;ll use the version provided by the Debian repo. I&#8217;ve followed [these instructions](https://engineerworkshop.com/blog/how-to-set-up-wireguard-on-a-raspberry-pi/):

```
sudo apt-get install dirmngr
echo "deb http://deb.debian.org/debian/ unstable main" | sudo tee --append /etc/apt/sources.list
sudo apt-key adv --keyserver   keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC
sudo apt-key adv --keyserver   keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
sudo sh -c 'printf "Package: *\nPin: release a=unstable\nPin-Priority: 90\n" > /etc/apt/preferences.d/limit-unstable'
sudo apt-get update
sudo apt install wireguard
```

I&#8217;ve transferred the created config from the WireGuard host to the WireGuard client and ran

```
sudo wg-quick up &lt;ProfileName>
```

And it established really fast a connection. However, my problem was now that the SSH connection broke because all of the traffic to and from the client was going through the WireGuard VPN (like you would have used it for your phone when you&#8217;re in an unsecured WiFi and want to redirect all traffic through the VPN).

Luckily I was able to stop the connection by SSHing from the WireGuard VPN to the assigned IP of the WireGuard client and by using

```
sudo wg-quick down &lt;ProfileName>
```

The question is now, how can I configure WireGuard Client to just know the route through the VPN to resources in the host network or vice versa how I can configure the WireGuard Host to provide other machines in the network a route to the connected client&#8230;