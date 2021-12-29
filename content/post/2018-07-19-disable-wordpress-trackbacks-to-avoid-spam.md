---
author: Centurio
categories:
- Blogs
date: "2018-07-19T08:11:23Z"
guid: http://centurio.net/?p=3203
id: 3203
tags:
- GDPR
- wordpress
title: Disable WordPress Trackbacks to avoid spam
url: /2018/07/19/disable-wordpress-trackbacks-to-avoid-spam/
---
I've intended to disable all comment or trackback functionality to avoid having spam and dealing with it in form of anti-spam plugins like Akismet. While I already had comments disabled, Trackbacks were still active.

Even when you disable Trackbacks in the WordPress settings via &#8222;Settings / Discussion&#8220; under &#8222;Allow link notifications from other Weblogs (Pingbacks and Trackbacks)&#8220;, your existing pages needs manual update to take effect.

Connect to your MySQL database of your blog (e.g. with PHPMyAdmin) and execute these two queries:

```lang-sql
UPDATE wp_posts set ping_status='closed' WHERE post_status='publish' AND post_type='post';
UPDATE wp_posts set ping_status='closed' WHERE post_status='publish' AND post_type='page';
```

&nbsp;

I've found this information on [Andreas blog](https://blog.thul.org/technik/anwendungen/pingbacks-und-trackbacks-global-abschalten/), thank you!