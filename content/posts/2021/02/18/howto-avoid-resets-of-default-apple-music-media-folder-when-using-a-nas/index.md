---
author: Centurio
categories:
- Apple
- NAS
date: "2021-02-18T10:15:30Z"
guid: https://centurio.net/?p=3446
id: 3446
tags:
- automount
title: Howto avoid resets of default Apple Music media folder when using a NAS

---
## Introduction
I'm a longtime fan and user of [automount](https://centurio.net/2016/03/16/automount-network-shares-on-mac-os-for-use-in-itunes/). Automount mounts automatically my Apple Music media folder, once the Music app tries to access it.

I've recently updated to a Macbook with apple Silicon running Big Sur. It looks like the default behaviour changed, because I'm often adding songs to Apple music, just to see that they are copied to my SSD instead of the automounted NAS media folder.

This is incredible annoying and is probably caused by a race condition between Apple Music and automount not mounting the volume fast enough. So from time to time I'll need to check my configured media folder in Apple music. I'll end up changing the folder back to the automount folder and need to wait for Apple music to finish a complete scan of the library:

{{< img "images/MusicUpdatingLibrary.png" "Apple Music Updating screen" >}}

### A workaround
[ "Limnos" pointed me](https://discussions.apple.com/thread/252216475) to a potential workaround for this behaviour:

  * Create a symbolic link to the Apple Music app on your SSD and place it on the automounted volume.
  * Create a second symbolic link from the first link back to your SSD applications folder.
  * Start Apple Music app only by using this link.
  * If the volume isn't mounted, the link will point nowhere and Apple Music won't start. This will hopefully stop it from rewriting the media paths.

This can be done in the terminal with just two commands:

```
ln -s /System/Applications/Music.app /System/Volumes/Data/mount/music/Music.app
ln -s /System/Volumes/Data/mount/music/Music.app /Applications/MusicOnNAS.app
```

You can now add that link to MusicOnNAS.app to your dock, but it can only be placed in the area next to the recycle bin.

You can test this now by unmounting the volume manually on the terminal. If you click now on the link in your dock, it won't start Apple Music. However, if you'll click it a second time, it will start since automount has successfully remounted your volume containing the link.

Nevertheless, Apple Music forgot its media path and I'll have to change it again to the folder. So this is just a bad workaround. Even when you'll change the media's path after this test, it will be reset on the next iTunes startup.

So ultimately I'll end up with a the instructions of  "[Make a split library portable](https://discussions.apple.com/docs/DOC-7392) ", which basically says you shouldn't separate the Apple Music library and its media. Always put the library next to the location of your media.

Also you'll need to make sure that you'll manually open the right .musiclibrary file. You can define the library to open when you hold the alt key before you'll start the Apple Music app:

{{< img "images/AppleMusicLibrarySelection.png" "Apple Music Library Selection screen" >}}

If you'll just double click, it will most likely not open the right library. Somehow macOS still knows where you've moved your local library file (e.g. to the NAS in the automounted folder) and will open it from the new location.

With moving the library next to the media I'm somehow happy about the outcome. Looks like Apple did not consider moving the Apple Music library to any external volume and expects it to be always present in a reachable location.