---
author: Centurio
categories:
- Apple
- NAS
date: "2020-10-26T23:15:56Z"
guid: https://centurio.net/?p=3405
id: 3405
tags:
- autofs
- Catalina
- itunes
title: Fix broken automount mounts on macOS Catalina

---
## Introduction
I've moved my iTunes music library content to my NAS. I'm using [automount](/page/search/?keyword=automount) to keep iTunes happy without losing the connection to the files. After upgrading to macOS Catalina, automount did not work as it used to.

### Changed structure of filesystem
Reason is the changed structure in the APFS container. If you have a look at the disk utility, it will show you a system container and a user container. The system contains macOS and is write protected, while the user container contains all your apps, data and so on.

You'll just have to [prepend your existing automount paths](https://www.fkylewright.com/2019/10/macos-catalina-10-15-autofs-mount-point-changes/) with /System/Volumes/Data. Now you'll just have to run

```
sudo automount -vc
```

and the automounts are working again.

I had to change the iTunes settings back to my automount folder, as the upgrade to Catalina reset it to its default location in your users folder.