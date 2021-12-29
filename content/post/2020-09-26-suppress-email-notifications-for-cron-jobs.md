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
url: /2020/09/26/suppress-email-notifications-for-cron-jobs/
---
After I&#8217;ve <a href="https://centurio.net/2020/09/21/configure-mail-transport-agent-on-raspbian-with-external-smtp-server/" data-type="post" data-id="3352">setup a proper MTA</a>, I received a lot of email notifications for my running cron jobs. However, I do not want to receive those emails and had to find a way to suppress them.

You can edit your crontab with

<pre class="wp-block-code"><code>crontab -e</code></pre>

Add at the top of the file:

<pre class="wp-block-code"><code>MAILTO=""</code></pre>

Emails won&#8217;t be send now.