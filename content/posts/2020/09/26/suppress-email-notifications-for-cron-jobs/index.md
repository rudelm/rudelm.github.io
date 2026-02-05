---
author: Centurio
categories:
- Linux
date: "2020-09-26T20:15:00Z"
guid: https://centurio.net/?p=3376
id: 3376
tags:
- cron
- email
title: Suppress email notifications for cron jobs

---
# Introduction
After I've [setup a proper MTA](/2020/09/21/configure-mail-transport-agent-on-raspbian-with-external-smtp-server/), I received a lot of email notifications for my running cron jobs. However, I do not want to receive those emails and had to find a way to suppress them.

## Enter crontab
You can edit your crontab with

```
crontab -e
```

Add at the top of the file:

```
MAILTO=""
```

Emails won't be send now.