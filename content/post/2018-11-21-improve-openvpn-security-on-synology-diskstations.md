---
author: Centurio
categories:
- Linux
- NAS
- Security
date: "2018-11-21T21:35:02Z"
guid: http://centurio.net/?p=3227
id: 3227
tags:
- OpenVPN
- Synology
title: Improve OpenVPN security on Synology DiskStations
url: /2018/11/21/improve-openvpn-security-on-synology-diskstations/
---
I&#8217;m using [OpenVPN on my Synology DiskStation with certificates](http://centurio.net/2014/12/23/how-to-use-client-certificates-with-synology-vpn-server-and-openvpn/) instead of Preshared Keys. A few days ago I&#8217;ve wanted to login to my VPN and it wasn&#8217;t working. After checking the log file I&#8217;ve seen that there were some issues with the used configuration file for OpenVPN.

<pre class="wp-block-code"><code>Tue Nov 20 23:04:27 2018 Cipher algorithm 'TLS-DHE-RSA-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-256-CB' not found
Tue Nov 20 23:04:27 2018 Exiting due to fatal error</code></pre>

How can this be? The configuration worked for months without problems? I&#8217;ve started to remember that I&#8217;ve started to increase the security of my OpenVPN configuration using a few parameters. The Cipher algorithm is one of them. [This page](https://stastka.ch/knowledge-base/OpenVPN-auf-einem-Synology-NAS-haerten/story/0f53abf5) describes some of the changes I&#8217;ve made (unfortunately only in German).

I&#8217;ve added the tls-cipher and tls-auth options as last parameter lines to my configuration file. The synology web UI tried to parse those parameters as cipher and auth parameter when it shows those values as part of the DSM UI.<figure class="wp-block-image">

<img loading="lazy" width="422" height="142" src="http://centurio.net/wp-content/uploads/2018/11/openvpn-dsm-settings.png" alt="" class="wp-image-3228" srcset="https://centurio.net/wp-content/uploads/2018/11/openvpn-dsm-settings.png 422w, https://centurio.net/wp-content/uploads/2018/11/openvpn-dsm-settings-300x101.png 300w" sizes="(max-width: 422px) 100vw, 422px" /> </figure> 

I&#8217;ve reorderded the tls-auth and tls-cipher parameter to be above the auth and cipher parameters and the DSM UI is now able to show those values correct. This will enable you to restart the OpenVPN service from the WebUI without the need to login via SSH.

How do you get supported values for auth, cipher and tls-cipher you might wonder? Just execute

<pre class="wp-block-code"><code>openvpn --show-tls</code></pre>

to get the supported tls-cipher you might line up with a : separated.

<pre class="wp-block-code"><code>openvpn --show-digests</code></pre>

shows you the allowed values for auth and

<pre class="wp-block-code"><code>openvpn --show-ciphers</code></pre>

will show the allowed values for cipher. However, cipher and auth can also be preselected from the DSM UI.

Don&#8217;t forget to use the same values in your OpenVPN configuration on your VPN client as well, otherwise the connection won&#8217;t work.