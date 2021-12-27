---
author: Centurio
categories:
- Linux
- Security
date: "2020-09-22T20:00:00Z"
guid: https://centurio.net/?p=3355
id: 3355
tags:
- Fail2ban
- Raspbian
- SSH
title: Protect SSH services with fail2ban
url: /2020/09/22/protect-ssh-services-with-fail2ban/
---
If you&#8217;ll open SSH on a server to the open internet, you&#8217;ll notice a lot of bots trying to login. You certainly should setup certificate based login, but banning offending IPs is also an important security measure.

I&#8217;ve installed fail2ban on my Raspbian installations and want to explain the installation and configuration. Its quite easy and the benefits are huge!

<pre class="wp-block-code"><code>sudo apt-get install fail2ban</code></pre>

Create a copy of the original configuration file so that it won&#8217;t be overwritten by any updates:

<pre class="wp-block-code"><code>sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local</code></pre>

Search for a block for [default]. You should set:

<pre class="wp-block-code"><code>bantime = 10m
findtime = 10m
maxretry = 5</code></pre>

These are the general settings. The settings for sshd should be a little bit stricter. Search a block for [sshd]. You should set:

<pre class="wp-block-code"><code>enabled = true
maxretry = 3</code></pre>

You can enable and start fail2ban now using systemctl:

<pre class="wp-block-code"><code>sudo systemctl enable fail2ban
sudo systemctl start fail2ban</code></pre>

Verify its up and running:

<pre class="wp-block-code"><code>sudo systemctl status fail2ban.service
sudo fail2ban-client status
sudo fail2ban-client status sshd</code></pre>

If you end up being locked out, you can unlog an offending IP address using this command:

<pre class="wp-block-code"><code>sudo fail2ban-client set sshd unbanip &lt;offenders IP&gt;</code></pre>

Banned connections will be dropped immediately by the firewall and should be visible with a &#8222;connection refused&#8220;.