---
author: Centurio
categories:
- Games
date: "2015-01-03T23:35:53Z"
guid: http://centurio.net/?p=2178
id: 2178
image: /2015/01/03/sync-borderlands-prequel-and-borderlands-2-savegames-between-mac-and-pc/Borderlands_2_play_time.png
tags:
- Borderlands
- Dropbox
- Mac
- Steam
title: Sync Borderlands Prequel and Borderlands 2 savegames between Mac and PC

---
# Introduction
I really liked Borderlands 2. So much, that I played over 42 hours already 🙂 This happened all on my gaming PC. With my new Macbook Pro and the availability of Borderlands for Mac, I intend to play it in LAN mode occasionally when I'm visiting friends who also play Borderlands. However, I was shocked when I started Steam on my Mac and did not see the savegames from my PC, although Steam's Cloud Synchronisation was active.

{{< img "images/Borderlands_2_Steam_Cloud_Sync.png" "Enable Steam Cloud sync" >}}

## The Problem
A short research showed that the developers of Borderlands had this feature deactivated, because they cannot guarantee that the correct patch versions are applied to all platforms to the same time. This could lead to possible corruption of the savegames and so they disabled Cloud Sync although it is activated by default:

> **Q: Will I be able to sync my game saves between the Windows PC, Mac, and Linux versions?**
> 
> A: Yes, but with a caveat: characters and saved games will NOT sync between Windows PC, Mac, and Linux via Steam Cloud.  Since the Mac and Linux versions of Borderlands: The Pre-Sequel may frequently be in an out of sync with the Windows PC version, syncing game saves across platforms via Steam Cloud has been disabled.  This will ensure saved game data will not be lost or corrupt due to incompatible in-game content or other unforeseen reasons.  Users do have the option of transferring game saves via physical media (like a thumb drive) if they wish.

 
## The Solution
Nevertheless, a [clever user on the steam forum](http://forums.steampowered.com/forums/showthread.php?t=3049227) created a nice tutorial. He intends to use Dropbox with NTFS and HFS+ symlinks to link the savegame folder to Dropbox. He suggests to use the mklink command this way:

```
mklink /d "C:\Users\YourUserName\Documents\My Games\Borderlands 2\WillowGame\SaveData\NumericalID" "C:\Users\YourUserName\Documents\Dropbox\DesiredFolder"
```

What he did miss to tell you is that you'll need an elevated command window with administrator rights. Just enter cmd on the Windows 8 start menu and select  "Open as administrator" on the command prompt.

The next problem is the order of the folders. In his order, this will result in an error message stating that the link could not be created. However, if you look up the command on [MSDN](http://technet.microsoft.com/en-us/library/cc753194%28v=ws.10%29.aspx) you'll see that you must switch the order of the arguments. It is first the Link name (in your Dropbox folder) and then the Target (What do you want to link).

All other information in that forum is correct. You'll need to link this numerical Id folder with your savegames to a Dropbox synced folder and do this also on the Mac. Be sure to create a backup before you create the links in case you overwrite your savegames. After that, it works. This will also work for Borderlands The Pre-Sequel!