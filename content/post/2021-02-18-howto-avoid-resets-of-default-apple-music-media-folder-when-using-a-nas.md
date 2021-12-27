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
url: /2021/02/18/howto-avoid-resets-of-default-apple-music-media-folder-when-using-a-nas/
---
I&#8217;m a longtime fan and user of [automount](https://centurio.net/2016/03/16/automount-network-shares-on-mac-os-for-use-in-itunes/). Automount mounts automatically my Apple Music media folder, once the Music app tries to access it.

I&#8217;ve recently updated to a Macbook with apple Silicon running Big Sur. It looks like the default behaviour changed, because I&#8217;m often adding songs to Apple music, just to see that they are copied to my SSD instead of the automounted NAS media folder.

This is incredible annoying and is probably caused by a race condition between Apple Music and automount not mounting the volume fast enough. So from time to time I&#8217;ll need to check my configured media folder in Apple music. I&#8217;ll end up changing the folder back to the automount folder and need to wait for Apple music to finish a complete scan of the library:<figure class="wp-block-image size-large"><a href="https://centurio.net/wp-content/uploads/2021/02/MusicUpdatingLibrary.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">

<img loading="lazy" width="452" height="239" src="https://centurio.net/wp-content/uploads/2021/02/MusicUpdatingLibrary.png" alt="" class="wp-image-3447" srcset="https://centurio.net/wp-content/uploads/2021/02/MusicUpdatingLibrary.png 452w, https://centurio.net/wp-content/uploads/2021/02/MusicUpdatingLibrary-300x159.png 300w" sizes="(max-width: 452px) 100vw, 452px" /> </a><figcaption>Waiting for Apple Music to update its library&#8230;</figcaption></figure> 

[&#8222;Limnos&#8220; pointed me](https://discussions.apple.com/thread/252216475) to a potential workaround for this behaviour:

  * Create a symbolic link to the Apple Music app on your SSD and place it on the automounted volume.
  * Create a second symbolic link from the first link back to your SSD applications folder.
  * Start Apple Music app only by using this link.
  * If the volume isn&#8217;t mounted, the link will point nowhere and Apple Music won&#8217;t start. This will hopefully stop it from rewriting the media paths.

This can be done in the terminal with just two commands:

<pre class="wp-block-code"><code>ln -s /System/Applications/Music.app /System/Volumes/Data/mount/music/Music.app
ln -s /System/Volumes/Data/mount/music/Music.app /Applications/MusicOnNAS.app</code></pre>

You can now add that link to MusicOnNAS.app to your dock, but it can only be placed in the area next to the recycle bin.

You can test this now by unmounting the volume manually on the terminal. If you click now on the link in your dock, it won&#8217;t start Apple Music. However, if you&#8217;ll click it a second time, it will start since automount has successfully remounted your volume containing the link.

Nevertheless, Apple Music forgot its media path and I&#8217;ll have to change it again to the folder. So this is just a bad workaround. Even when you&#8217;ll change the media&#8217;s path after this test, it will be reset on the next iTunes startup.

So ultimately I&#8217;ll end up with a the instructions of &#8222;[Make a split library portable](https://discussions.apple.com/docs/DOC-7392)&#8222;, which basically says you shouldn&#8217;t separate the Apple Music library and its media. Always put the library next to the location of your media.

Also you&#8217;ll need to make sure that you&#8217;ll manually open the right .musiclibrary file. You can define the library to open when you hold the alt key before you&#8217;ll start the Apple Music app:<figure class="wp-block-image size-large"><a href="https://centurio.net/wp-content/uploads/2021/02/AppleMusicLibrarySelection.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">

<img loading="lazy" width="744" height="856" src="https://centurio.net/wp-content/uploads/2021/02/AppleMusicLibrarySelection.png" alt="" class="wp-image-3448" srcset="https://centurio.net/wp-content/uploads/2021/02/AppleMusicLibrarySelection.png 744w, https://centurio.net/wp-content/uploads/2021/02/AppleMusicLibrarySelection-261x300.png 261w" sizes="(max-width: 744px) 100vw, 744px" /> </a><figcaption>Apple Music asks for a library to use when you&#8217;ll open it with alt key pressed.</figcaption></figure> 

If you&#8217;ll just double click, it will most likely not open the right library. Somehow macOS still knows where you&#8217;ve moved your local library file (e.g. to the NAS in the automounted folder) and will open it from the new location.

With moving the library next to the media I&#8217;m somehow happy about the outcome. Looks like Apple did not consider moving the Apple Music library to any external volume and expects it to be always present in a reachable location.