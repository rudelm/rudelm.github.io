---
author: Centurio
categories:
- Apple
date: "2019-10-16T23:16:34Z"
guid: http://centurio.net/?p=3287
id: 3287
image: /wp-content/uploads/2019/10/Screenshot-2019-10-16-at-23.04.29.png
tags:
- Catalina
- Mojave
- Notifications
- Update
title: Disable macOS Catalina update notification in Mojave
url: /2019/10/16/disable-macos-catalina-update-notification-in-mojave/
---
macOS Catalina was released and is ready to install. If you&#8217;re using the previous macOS version called Mojave, you&#8217;ll get a notification badge on the system settings. 

This little red notification badge is really annoying.

The following two commands were taken from the [Apple support forum](https://discussions.apple.com/thread/250711218):

<pre class="wp-block-code"><code>sudo softwareupdate --ignore "macOS Catalina"</code></pre>

If you want to install Catalina via the software update, you can reset the ignored updates with this command:

<pre class="wp-block-code"><code>sudo softwareupdate --reset-ignored</code></pre>

This will hide successfully the Catalina update from the list of available updates in Software Update. However, it won&#8217;t remove the notification badge.

But fortunately you can even disable the badge by using [these commands](https://dev.to/krnsk0/turn-off-macos-badge-update-notifications-4bip):

<pre class="wp-block-code"><code>defaults write com.apple.systempreferences AttentionPrefBundleIDs 0
killall Dock</code></pre>

This will hide the badge until the next time you&#8217;ll scan for available software updates.