---
author: Centurio
categories:
- Apple
date: "2021-01-15T23:36:04Z"
guid: https://centurio.net/?p=3439
id: 3439
tags:
- MacBookPro
- SATA
- SSD
title: Slow SSDs in MacBook Pro 13" 2012
url: /2021/01/15/slow-ssds-in-macbook-pro-13-2012/
---
A friend asked me to check her MacBook Pro 13" from 2012. It is running unbearable slow. So I've made a bootable copy with Carbon Copy Cloner and TimeMachine and tried to start with a fresh installation.

I've created an external Bootdisk with macOS 10.15 and tried to repartition and wipe the SSD. This process took already very long and I started to wonder what might have caused this delay.

This MacBook was running fine for almost two years when I've replaced the internal HDD with a SanDisk SSD Plus SDSSDA-480G. All the more I was wondering why it started to be so slow without warning.

I've found [this post](https://www.ifixit.com/Answers/View/519420/MacBook+is+slow+after+upgrading+to+SSD) on [ifixit.com](https://www.ifixit.com/Answers/View/236761/SSD+Became+Very+Slow) where someone replaced the HDD with an SSD in the same model and it started to be very slow. The culprit [should be the internal SATA cable](https://apple.stackexchange.com/questions/177603/ridiculously-slow-macbook-pro), which isn't either SATA3 compatible or [has broken data lanes](https://boards.rossmanngroup.com/threads/why-the-821-1480-and-821-2049-hard-drive-cables-die.17992/) due to mechanic stress from bending or itching on sharp edges caused by the CNC milling of the MacBook case:<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure> 

I've checked the cable and did not see any damages to the cable. So I've tried an old HDD on the same cable and repartitioning and installing was reasonable fast again.

I was still not convinced that the cable should be the problem, but decided to order a new cable including the IR receiver as well as the standby LED. There's [some sort of confusion](https://www.ifixit.com/Answers/View/467903/Latest+Version+HDD+SATA+Cable+Replacement+13%22) about the right model number, but looks like 821-1480-A is the right one. I've ordered the cable from [iFixit.com](https://store.ifixit.de/products/macbook-pro-13-unibody-mid-2012-hard-drive-cable?variant=31817322725461) as I intended to avoid quality problems. However, you'll get the same cable with the HDD bracket for less money from [Amazon](https://www.ifixit.com/Answers/View/467903/Latest+Version+HDD+SATA+Cable+Replacement+13%22).

[Replacing the cable](https://www.ifixit.com/Guide/MacBook+Pro+13-Inch+Unibody+Mid+2012+Hard+Drive+Cable+Replacement/10379) is quite easy and can be done in less than 10 minutes.

After I've replaced the cable, I've tried the SanDisk SSD again. The installation was still very slow so I've cancelled the installation. Luckily I've had another SSD which I could test and this one installed quite fast.

So I've decided to replace the exchanged cable with the original cable and rebooted the Mac. I was surprised by a login screen where the default user was unknown. I've only created one user on that machine and it should've been automatically preselected. Ok, I can type that username by myself and typed the password, but I'm unable to login at all. Either password or username are wrong?!

I've rebooted to the recovery partition of the currently installed SSD and tried to repartition the SSD. Deletion was now slow again and failed with this error I've never seen before (got the error message only in German, sorry 😞):

<blockquote class="wp-block-quote">
  <p>
    Das Entfernen der Volumedaten zum Verhindern zukünftiger unbeabsichtigter Überprüfungen ist fehlgeschlagen (-69825).
  </p>
</blockquote>

Searching for this error lead me to [a German forum](https://www.apfeltalk.de/community/threads/ssd-laesst-sich-nicht-formatieten-festplattendienstprogramm.507817/), where a user has also the same MacBook and problems with his SSD. Looks like changing the SATA cable helped in this case.

After I've replaced the faulty SATA cable with the new one, I was able to repartition the SSD which wasn't deletable before.