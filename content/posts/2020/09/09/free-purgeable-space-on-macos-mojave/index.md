---
author: Centurio
categories:
- Apple
date: "2020-09-09T21:06:04Z"
guid: https://centurio.net/?p=3344
id: 3344
tags:
- APFS
- Mac OS
title: Free purgeable space on MacOS Mojave

---
## Introduction
I've recently deleted a large preview database file for Lightroom and was happy about the 80GB won free space. However, the MacOS disk utility as well as the terminal command  "df -h" did not show the free space. I've also checked the trash and cleared it, but there was no change in the available disk space.

### Disk Utility
I've taken a closer look at the free space column in the disk utility and found a new variable behind the available disk space: GB purgeable.

{{< img "images/purgeableSpaceMacOSDiskUtility.png" "Purgeable space in Disk utility" >}}

However, there is nowhere an option to purge this space. Upon further searching I've found [this tip on stack overflow](https://apple.stackexchange.com/a/398356/19241):

### TimeMachine is the culprit
It looks like TimeMachine takes up a lot of free space in APFS snapshots which needs manual cleaning using this command:

```
tmutil thinlocalsnapshots / $((100 * 1024 * 1204 * 1024)) 4
```

This command tries to free 100GB space from the local snapshots. It's using the highest priority (4) to speed up the cleaning.

After I've executed that command, the available free disk space was shown correctly again.