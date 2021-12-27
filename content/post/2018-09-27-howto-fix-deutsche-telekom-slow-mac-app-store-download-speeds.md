---
author: Centurio
categories:
- Apple
date: "2018-09-27T22:22:04Z"
guid: http://centurio.net/?p=3208
id: 3208
tags:
- DNS
- Mac OS X
- Mojave
title: Howto fix Deutsche Telekom slow Mac App Store download speeds
url: /2018/09/27/howto-fix-deutsche-telekom-slow-mac-app-store-download-speeds/
---
macOS Mojave was released to the public on Monday. As I&#8217;m still suffering under terrible problems with macOS High Sierra Updates, I&#8217;ve decided to give my Mac a chance and to download Mojave.



<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="460" height="388" src="http://centurio.net/wp-content/uploads/2018/09/MacOS-Mojave.png" alt="" class="wp-image-3209" srcset="https://centurio.net/wp-content/uploads/2018/09/MacOS-Mojave.png 460w, https://centurio.net/wp-content/uploads/2018/09/MacOS-Mojave-300x253.png 300w" sizes="(max-width: 460px) 100vw, 460px" /><figcaption>macOS Mojave installer start screen<br /></figcaption></figure>
</div>

I&#8217;ve started the download from the Mac App Store and the download speed was really slow. I&#8217;m using a 50MBit VDSL connection provided by the Deutsche Telekom. All other Downloads are fast and saturate the connection at about 5,5MB/s.



<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="841" height="246" src="http://centurio.net/wp-content/uploads/2018/09/mojave-slow-download.png" alt="" class="wp-image-3210" srcset="https://centurio.net/wp-content/uploads/2018/09/mojave-slow-download.png 841w, https://centurio.net/wp-content/uploads/2018/09/mojave-slow-download-300x88.png 300w, https://centurio.net/wp-content/uploads/2018/09/mojave-slow-download-768x225.png 768w" sizes="(max-width: 841px) 100vw, 841px" /><figcaption>Really slow downloads from the App Store. This one should download for 5 and a half hour</figcaption></figure>
</div>

The Download from the Mac App Store is terribly slow at around 200kB/s. After searching for problems with Deutsche Telekom and slow App Store speeds, I&#8217;ve stumbled over [this page](https://www.macgadget.de/Forum/Mac-App-Store-Downloads-mit-Trick-beschleunigen).

The solution to my slow download rates seem to be the used DNS server. Even if you use the DNS from Quad9 or the one from Google, you will have slow downloads.

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="825" height="254" src="http://centurio.net/wp-content/uploads/2018/09/mojave-fast-download.png" alt="" class="wp-image-3211" srcset="https://centurio.net/wp-content/uploads/2018/09/mojave-fast-download.png 825w, https://centurio.net/wp-content/uploads/2018/09/mojave-fast-download-300x92.png 300w, https://centurio.net/wp-content/uploads/2018/09/mojave-fast-download-768x236.png 768w" sizes="(max-width: 825px) 100vw, 825px" /><figcaption>A fast download from the App Store with 5,5MB/s. It finishes in 22 minutes</figcaption></figure>
</div>

The recommended IPv4 DNS server are quite fast. I&#8217;ve setup a new Network Profile with these DNS server and I have now the full download speed again.

<div class="wp-block-image">
  <figure class="aligncenter"><img loading="lazy" width="320" height="458" src="http://centurio.net/wp-content/uploads/2018/09/faster-dns-settings.png" alt="" class="wp-image-3212" srcset="https://centurio.net/wp-content/uploads/2018/09/faster-dns-settings.png 320w, https://centurio.net/wp-content/uploads/2018/09/faster-dns-settings-210x300.png 210w" sizes="(max-width: 320px) 100vw, 320px" /></figure>
</div>

You can switch your network profile afterwards to your local DNS server.