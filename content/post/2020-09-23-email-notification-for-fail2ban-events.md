---
author: Centurio
categories:
- Linux
- Security
date: "2020-09-23T20:25:38Z"
guid: https://centurio.net/?p=3374
id: 3374
tags:
- email
- Fail2ban
title: Email notification for fail2ban events
url: /2020/09/23/email-notification-for-fail2ban-events/
---
So I&#8217;ve configured <a href="https://centurio.net/2020/09/22/protect-ssh-services-with-fail2ban/" data-type="post" data-id="3355">my fail2ban installation</a> and I&#8217;m also able to <a href="https://centurio.net/2020/09/21/configure-mail-transport-agent-on-raspbian-with-external-smtp-server/" data-type="post" data-id="3352">send emails</a>. But wouldn&#8217;t it be awesome if I&#8217;ll get notified via email about any fail2ban event?

We start with editing the /etc/fail2ban/jail.local file. Look for the destemail and action parameters and change them accordingly:

```
mta = sendmail
destemail = recipient@domain.name
senderemail = sender@domain.name
action = %(action_mwl)s
```

The action can be one of these, whereby I&#8217;ve chosen action_mwl:

  * action_: ban only the IP
  * action_mw: ban the IP and send email with whois information about the banned IP
  * action_mwl:&nbsp;ban the IP and send email with whois information about the banned IP and add relevant log lines to the email
  * action\_cf\_mwl: notify Cloudfare about the offending IP, ban the IP and send email with whois information about the banned IP

Do a restart of fail2ban:

```
sudo systemctl restart fail2ban
```

You&#8217;ll receive a lot of emails from fail2ban. This also includes any starts and stops of fail2ban as well as the ban notifications. You can limit this behavior by adding following content to the file /etc/fail2ban/action.d/mail-buffered.local:

```
[Definition]

# Option:  actionstart
# Notes.:  command executed once at the start of Fail2Ban.
# Values:  CMD
#
actionstart =

# Option:  actionstop
# Notes.:  command executed once at the end of Fail2Ban
# Values:  CMD
#
actionstop =
```

Now copy this file a few times with different file names:

```
sudo cp /etc/fail2ban/action.d/mail-buffered.local /etc/fail2ban/action.d/mail.local
sudo cp /etc/fail2ban/action.d/mail-buffered.local /etc/fail2ban/action.d/mail-whois-lines.local
sudo cp /etc/fail2ban/action.d/mail-buffered.local /etc/fail2ban/action.d/mail-whois.local
sudo cp /etc/fail2ban/action.d/mail-buffered.local /etc/fail2ban/action.d/sendmail-buffered.local
sudo cp /etc/fail2ban/action.d/mail-buffered.local /etc/fail2ban/action.d/sendmail-common.local
```

Do a restart of fail2ban:

```
sudo systemctl restart fail2ban
```

You should now only receive emails for ban events.