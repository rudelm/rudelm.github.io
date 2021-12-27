---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2020-09-24T20:39:34Z"
guid: https://centurio.net/?p=3382
id: 3382
tags:
- SSH
title: Block SSH connections by origin of IP address
url: /2020/09/24/block-ssh-connections-by-origin-of-ip-address/
---
If you&#8217;re exposing services to the internet, you&#8217;ll notice a lot of connection attempts. To block those bots and scripts trying to login to your machine, you should use <a href="https://centurio.net/2020/09/22/protect-ssh-services-with-fail2ban/" data-type="post" data-id="3355">fail2ban</a>.

However, you can also limit the range of allowed origins of the IP addresses. The company MaxMind provides a database of IP addresses and their origin contries. You can configure your machine in such a way that only certain country codes are allowed.

Start by installing the geoip client and database by using this apt command:

<pre class="wp-block-code"><code>sudo apt-get install geoip-bin geoip-database</code></pre>

This database is updated automatically, when you&#8217;ve got your machine configured for auto updates.

The next step is to save this script to your machine in /usr/local//usr/local/bin/ipfilter.sh:

Edit the script to your needs, e.g. by limiting the number of allowed countries. Now make this script executable:

<pre class="wp-block-code"><code>chmod +x /usr/local/bin/ipfilter.sh</code></pre>

It is time to test it. Try the command with a known IP in America and one from a local network or known IP from the allowed countries:

<pre class="wp-block-code"><code>> /usr/local/bin/ipfilter.sh
Usage:  ipfilter.sh &lt;ip>
> /usr/local/bin/ipfilter.sh 8.8.8.8
> echo $?
1
> /usr/local/bin/ipfilter.sh 192.168.1.1
> echo $?
0</code></pre>

Notice the different exit codes of the script. If the IP is from a country that is allowed or if it is from a local network, it will exit with 0, otherwise 1. We can use this script now to configure a filter for sshd in the /etc/hosts.allow and /etc/hosts.deny files.

Add to /etc/hosts.allow:

<pre class="wp-block-code"><code>sshd: ALL: aclexec /usr/local/bin/ipfilter.sh %a
</code></pre><figure class="wp-block-pullquote">

> As documented in the `hosts_options(5)` man page, the standard output is redirected to `/dev/null`, so that there&#8217;s no chance for you to get the output from `echo`. And as you want the exit status to be taken into account, you should use `aclexec` instead of `spawn`. Indeed the man page says for `aclexec`: &#8222;The connection will be allowed or refused depending on whether the command returns a true or false exit status.&#8220;
> 
> <cite>https://unix.stackexchange.com/a/149057/298669</cite></figure> 

I&#8217;ve previously used &#8222;spawn&#8220; instead of &#8222;aclexec&#8220; but the IPs weren&#8217;t blocked. There were still connection attempts in the fail2ban log. By using aclexec, the exit code will be properly used for filtering.

Add to /etc/hosts.deny:

<pre class="wp-block-code"><code>sshd: ALL
</code></pre>

Please note the trailing newline. If this is the last entry in the hosts file, you&#8217;ll need to add a newline. Otherwise the role won&#8217;t be active.

Do a reboot of your machine and try to connect. You should still be able to connect 😉 Otherwise you&#8217;ll need to revert this changes locally, since you&#8217;ve successfully blocked yourself from accessing that machine.

You can have a look at the /var/log/auth.log and will see entries like this for example (blocking an IP from China/CN):

<pre class="wp-block-code"><code>Sep 30 12:10:32 raspberrypi root: DENY sshd connection from 222.186.30.76 (CN)
Sep 30 12:10:32 raspberrypi sshd&#91;886]: aclexec returned 1
Sep 30 12:10:32 raspberrypi sshd&#91;886]: refused connect from 222.186.30.76 (222.186.30.76)</code></pre>

This should reduce the amount of blocked SSH connections attempts significantly, if configured to a smaller selection of countries.