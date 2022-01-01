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
macOS Catalina was released and is ready to install. If you're using the previous macOS version called Mojave, you'll get a notification badge on the system settings. 

This little red notification badge is really annoying.

The following two commands were taken from the [Apple support forum](https://discussions.apple.com/thread/250711218):

```
sudo softwareupdate --ignore "macOS Catalina"
```

If you want to install Catalina via the software update, you can reset the ignored updates with this command:

```
sudo softwareupdate --reset-ignored
```

This will hide successfully the Catalina update from the list of available updates in Software Update. However, it won't remove the notification badge.

But fortunately you can even disable the badge by using [these commands](https://dev.to/krnsk0/turn-off-macos-badge-update-notifications-4bip):

```
defaults write com.apple.systempreferences AttentionPrefBundleIDs 0
killall Dock
```

This will hide the badge until the next time you'll scan for available software updates.