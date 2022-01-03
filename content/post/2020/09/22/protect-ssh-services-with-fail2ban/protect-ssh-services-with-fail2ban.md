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
If you'll open SSH on a server to the open internet, you'll notice a lot of bots trying to login. You certainly should setup certificate based login, but banning offending IPs is also an important security measure.

I've installed fail2ban on my Raspbian installations and want to explain the installation and configuration. Its quite easy and the benefits are huge!

```
sudo apt-get install fail2ban
```

Create a copy of the original configuration file so that it won't be overwritten by any updates:

```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

Search for a block for [default]. You should set:

```
bantime = 10m
findtime = 10m
maxretry = 5
```

These are the general settings. The settings for sshd should be a little bit stricter. Search a block for [sshd]. You should set:

```
enabled = true
maxretry = 3
```

You can enable and start fail2ban now using systemctl:

```
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

Verify its up and running:

```
sudo systemctl status fail2ban.service
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

If you end up being locked out, you can unlog an offending IP address using this command:

```
sudo fail2ban-client set sshd unbanip &lt;offenders IP&gt;
```

Banned connections will be dropped immediately by the firewall and should be visible with a  "connection refused".