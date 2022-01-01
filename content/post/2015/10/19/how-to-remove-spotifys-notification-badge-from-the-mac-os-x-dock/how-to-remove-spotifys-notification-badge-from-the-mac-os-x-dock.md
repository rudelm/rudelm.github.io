---
author: Centurio
categories:
- Apple
date: "2015-10-19T23:02:37Z"
guid: http://centurio.net/?p=2260
id: 2260
image: /wp-content/uploads/2015/10/Screen-Shot-2015-10-18-at-21.29.54.png
tags:
- Mac OS X
- Notifications
- Spotify
- UX
title: How to remove Spotify's notification badge from the Mac OS X dock
url: /2015/10/19/how-to-remove-spotifys-notification-badge-from-the-mac-os-x-dock/
---
Are you also annoyed and tired by Spotify's notification badge in the dock of Mac OS X? I totally was and found a simple list of instructions on [apple.stackexchange.com](http://apple.stackexchange.com/questions/153182/remove-dock-notification-badge-for-apps-not-in-notification-center/194316#194316)&nbsp;and want to show you how to remove this &#8222;feature".

If correctly used, notification badges are a cool thing. They notify you when an app wants your attention. Spotify abuses this feature and shows the number of pending notifications inside its app. That means: If you ever subscribed to somebodies playlist and this playlist is updated, you will be notified. Same goes for stuff like new tracks of your favorited artists. You have no control over these notifications and will always be notified. [Other](https://community.spotify.com/t5/Help-Accounts-and-Subscriptions/Disable-Notifications/td-p/147336) [users](https://community.spotify.com/t5/Help-Desktop-Mac/Disabling-Mac-OS-X-Dock-badge-notifications-about-additions-to/m-p/609362#M3325) are also annoyed&nbsp;by this misbehavior but nothing changes 🙁 Thats why my Spotify is mostly minimized to the background and when opened it shows this ugly notification badge in its UI:

<a href="http://centurio.net/wp-content/uploads/2015/10/Screen-Shot-2015-10-18-at-21.30.04.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-full wp-image-2261" src="http://centurio.net/wp-content/uploads/2015/10/Screen-Shot-2015-10-18-at-21.30.04.png" alt="Spotify in app notification badge" width="124" height="56" /></a>

Its annoying and always tries to steal my attention. Same goes for the Mac OS X dock icon:

<a href="http://centurio.net/wp-content/uploads/2015/10/Screen-Shot-2015-10-18-at-21.29.54.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-full wp-image-2262" src="http://centurio.net/wp-content/uploads/2015/10/Screen-Shot-2015-10-18-at-21.29.54.png" alt="Spotify Dock Icon with 99 notifications" width="96" height="92" /></a>

Normally, you can open the system preferences and can disable the notifications. However, Spotify isn't listed (although it uses the notification APIs of Mac OS X).

The instructions from stackoverflow write this missing entry into the notification database, so that it shows up in the list. Only after that you are allowed to disable Dock notifications:

<a href="http://centurio.net/wp-content/uploads/2015/10/DisableSpotifyBadgeAppIcon.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2263" src="http://centurio.net/wp-content/uploads/2015/10/DisableSpotifyBadgeAppIcon-300x237.png" alt="Disable Spotify Badge App Icon" width="300" height="237" srcset="https://centurio.net/wp-content/uploads/2015/10/DisableSpotifyBadgeAppIcon-300x237.png 300w, https://centurio.net/wp-content/uploads/2015/10/DisableSpotifyBadgeAppIcon.png 669w" sizes="(max-width: 300px) 100vw, 300px" /></a>&nbsp;Here's the code of Ryan Patterson's stackoverflow entry, in case it ever gets deleted:

```lang-bash
# "Usernoted" seems to be the "user notifications daemon", so get it's PID.
pid=$(ps aux | grep -i [u]sernoted | awk '{print $2}')

# Find the sqlite3 database that this program has open. It's in a "private" folder (app sandboxing).
db="$(lsof -p $pid | grep com.apple.notificationcenter/db/db\$ | awk '{print $9}')"

# I got the bundleid from Spotify.app/Contents/Info.plist
bundleid="com.spotify.client"

# I use 0 as the flags because you can change all the settings in System Preferences
# 5 seems to be the default for show_count
# Grab the next-highest sort order
sql="INSERT INTO app_info (bundleid, flags, show_count, sort_order) VALUES ( '$bundleid', 0, 5, (SELECT MAX(sort_order) + 1 FROM app_info) );"

# Run the command
sqlite3 "$db" "$sql"

# Restart usernoted to make the changes take effect
killall usernoted
```

&nbsp;