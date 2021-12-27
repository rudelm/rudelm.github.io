---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2018-10-28T14:28:42Z"
guid: http://centurio.net/?p=3220
id: 3220
tags:
- autofs
- Raspbian
title: Howto ensure automatically mounted NFS volume on Raspbian Stretch
url: /2018/10/28/howto-ensure-automatically-mounted-nfs-volume-on-raspbian-stretch/
---
**Update**: [I&#8217;m doing the automated mount now with autofs](http://centurio.net/2018/11/21/auto-mount-nfs-shares-on-raspbian/).

I&#8217;ve tried to setup NFS on my old Raspberry Pi 1 with Raspbian Stretch. I assumed that I just need to add an entry to the /etc/fstab file and the NFS volume on my Synology NAS would be mounted automatically.

So I&#8217;ve added this

<pre class="wp-block-code"><code>mynas:/volume1/databases /mnt/databases nfs defaults 0 0</code></pre>

and thought I would be done. I&#8217;ve created the /mnt/databases folder with

<pre class="wp-block-code"><code>mkdir /mnt/databases</code></pre>

and tried to mount everything with

<pre class="wp-block-code"><code>mount -a</code></pre>

and my volume showed up as mounted. After reboot the volume wasn&#8217;t mounted anymore and the service couldn&#8217;t find its data. So what shall we do? After some research I&#8217;ve found these options, which fixed the problem:

<pre class="wp-block-code"><code>mynas:/volume1/databases /mnt/databases nfs defaults,noauto,x-systemd.automount 0 0</code></pre>

The NFS volume now shows up even after a reboot. I&#8217;ve also tried to change the configuration of Raspbian so that it waits for the network before any services start but that didn&#8217;t fix the problem. Interestingly the entry with only defaults seems to be working on a Raspberry Pi 3 B.