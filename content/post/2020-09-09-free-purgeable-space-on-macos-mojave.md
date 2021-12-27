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
url: /2020/09/09/free-purgeable-space-on-macos-mojave/
---
I&#8217;ve recently deleted a large preview database file for Lightroom and was happy about the 80GB won free space. However, the MacOS disk utility as well as the terminal command &#8222;df -h&#8220; did not show the free space. I&#8217;ve also checked the trash and cleared it, but there was no change in the available disk space.

I&#8217;ve taken a closer look at the free space column in the disk utility and found a new variable behind the available disk space: GB purgeable.<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="309" src="https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility-1024x309.png" alt="" class="wp-image-3345" srcset="https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility-1024x309.png 1024w, https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility-300x91.png 300w, https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility-768x232.png 768w, https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility-1536x464.png 1536w, https://centurio.net/wp-content/uploads/2020/09/purgeableSpaceMacOSDiskUtility.png 1822w" sizes="(max-width: 1024px) 100vw, 1024px" /> </figure> 

However, there is nowhere an option to purge this space. Upon further searching I&#8217;ve found [this tip on stack overflow](https://apple.stackexchange.com/a/398356/19241):

It looks like TimeMachine takes up a lot of free space in APFS snapshots which needs manual cleaning using this command:

<pre class="wp-block-code"><code>tmutil thinlocalsnapshots / $((100 * 1024 * 1204 * 1024)) 4</code></pre>

This command tries to free 100GB space from the local snapshots. It&#8217;s using the highest priority (4) to speed up the cleaning.

After I&#8217;ve executed that command, the available free disk space was shown correctly again.