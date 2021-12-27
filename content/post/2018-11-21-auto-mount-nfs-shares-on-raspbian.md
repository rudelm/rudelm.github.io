---
author: Centurio
categories:
- Linux
- NAS
- Raspberry Pi
date: "2018-11-21T23:07:23Z"
guid: http://centurio.net/?p=3231
id: 3231
tags:
- autofs
- InfluxDB
title: Auto mount NFS shares on Raspbian
url: /2018/11/21/auto-mount-nfs-shares-on-raspbian/
---
I&#8217;m using influxdb on my Raspberry Pi in combination with a NFS mount. The NFS mount is on my Synology NAS and should store the database data of influxdb. Reason for this setup is that I fear that the SD card won&#8217;t survive the many write/read cycles caused by a database writing to it.

The shared folder on my Synology is configured to be accessible by various IPs in my network:<figure class="wp-block-image">

<img loading="lazy" width="862" height="569" src="http://centurio.net/wp-content/uploads/2018/11/synology-nfs-settings.png" alt="" class="wp-image-3232" srcset="https://centurio.net/wp-content/uploads/2018/11/synology-nfs-settings.png 862w, https://centurio.net/wp-content/uploads/2018/11/synology-nfs-settings-300x198.png 300w, https://centurio.net/wp-content/uploads/2018/11/synology-nfs-settings-768x507.png 768w" sizes="(max-width: 862px) 100vw, 862px" /> </figure> 

The problem with Raspbian is that [I&#8217;ve tried to auto mount the NFS share on startup](http://centurio.net/2018/10/28/howto-ensure-automatically-mounted-nfs-volume-on-raspbian-stretch/), so that the influxdb service can directly write to the NFS mount. 

I&#8217;ve used these settings in my /etc/fstab to mount the volume automatically:

<pre class="wp-block-code"><code>&lt;DS IP>:/volume1/databases /mnt/databases nfs auto,user,rw,nolock,nosuid 0 0</code></pre>

This doesn&#8217;t work properly since my influxdb is often dead after a restart, but if I check the mounted volumes I see the NFS volume mounted properly.

However, there&#8217;s a tool called autofs [which already helped me](http://centurio.net/2016/03/16/automount-network-shares-on-mac-os-for-use-in-itunes/) with a similar problem on my Mac when I moved my iTunes library to the Synology share.

Install autofs using

<pre class="wp-block-code"><code>sudo apt-get install autofs</code></pre>

Open the file /etc/auto.master and add something like this

<pre class="wp-block-code"><code>/mnt    /etc/auto.databases     -nosuid,noowners</code></pre>

Now create a file called /etc/auto.databases with this content

<pre class="wp-block-code"><code>databases       -fstype=nfs,user,nolock,nosuid,rw &lt;DS IP>:/volume1/databases</code></pre>

Unmount the existing NFS share. Remove/comment out the line for the nfs mount in your /etc/fstab so that it doesn&#8217;t conflict with autofs. Restart autofs with

<pre class="wp-block-code"><code>sudo service autofs restart</code></pre>

Now check the content of your mount point with e.g.

<pre class="wp-block-code"><code>ls /mnt/databases</code></pre>

Autofs should now automatically mount the NFS share. This might take a while, which is a good sign that the mount is loaded. You can also verify with

<pre class="wp-block-code"><code>mount</code></pre>

that your NFS share is mounted to e.g. /mnt/databases. If you&#8217;ll restart now, influxdb should be happy on restart. When it tries to start, autofs will see the access to the mounted folder and will mount the NFS share before influxdb can start up properly.