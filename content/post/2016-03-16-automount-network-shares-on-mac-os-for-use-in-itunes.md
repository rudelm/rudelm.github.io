---
author: Centurio
categories:
- Apple
- NAS
date: "2016-03-16T19:39:50Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=2286
id: 2286
tags:
- autofs
- Mac
- Synology
title: Automount network shares on Mac OS for use in iTunes
url: /2016/03/16/automount-network-shares-on-mac-os-for-use-in-itunes/
---
<div class="wp-block-group">
  <div class="wp-block-group__inner-container">
  </div>
</div>

I&#8217;ve moved my iTunes library from my Macbook&#8217;s SSD to my [Synology NAS](http://centurio.net/?s=synology) on a network share. This is quite easy and can be made inside the iTunes preferences pane. After you&#8217;ve changed the path for the iTunes Media, all iTunes managed media will be moved to the new location (assuming you let iTunes manage your files of course :)).

This allows you to have your iTunes library on your Macbook while all the large files are stored on the NAS. This is especially important for larger libraries as well as the newer Macbooks which only have a limited flash drive instead of larger harddisks.

However, there is one important problem with this solution: Once you&#8217;ve disconnected from this network share for whatever reasons and you try to start iTunes, you&#8217;ll have your iTunes Media folder reset to your user&#8217;s music folder on your boot disk. You&#8217;ll now need to reset the path to your files again, and this will again cause iTunes to check all files if they are on the right location and moves them if necessary.

I thought I&#8217;ve taken care of this problem with auto connecting to the network share with a Login Item. However, this didn&#8217;t help me much since I sometimes have disconnections to my network (e.g. when I&#8217;m on the road) and the network connection will only be created once during the login of your current user. So this doesn&#8217;t help me at all and caused me to look for another better solution.

So I&#8217;ve found <del>this gist</del> (the link is dead) and modified it a little bit to my environment. Therefore here&#8217;s my short list of modifications for using autofs in combination with AFP or SMB volumes:

If you now start up iTunes again, it will try to locate the media files in the /Volumes/music folder, like I manually specified it. However, autofs will now automatically mount the network share for me and iTunes won&#8217;t complain about a missing volume. This way I won&#8217;t ever need to take care of manually updating the path once I forgot connecting to my NAS 🙂

**Update:**  
Hm, it seems that the trick with /../Volumes does not work anymore on Mac OS 10.11.4 🙁 If I try to list the content of the mounted volume an error message is returned:

`ls: : Unknown error: 118`

So I need to mount the volume in a different folder and need to change the path in iTunes again.

**Update 2:**  
I&#8217;m not able to mount afp volumes anymore so I&#8217;m using smbfs like it is described [<del>here</del> (the link is dead)](https://www.dforge.net/2012/08/07/create-a-permanent-smb-mount-in-osx/). However, this will require a user and password in the configuration file 🙁

**Update 3:**

Mac OS Sierra breaks the autofs configuration. I had to change it a little bit according to [this&nbsp;SuperUser entry](http://superuser.com/questions/997735/how-to-mount-smb-share-that-can-be-accessed-by-anyone-on-mac-os-x-el-capitan). The Gist is updated accordingly.

**Update 4:**

This still works on Mac OS High Sierra. However, make sure that you enter the credentials correctly and that you spare special characters, according to [this blog](https://derflounder.wordpress.com/2014/04/06/using-etcauto_home-on-mavericks-to-mount-shares-under-home/):

**<u>Note:</u>**&nbsp;If you have a password longer than 8 characters, or if the password has special characters in it (like “! # $ % & ‘ ( ) * + , – . / : ; & < = > ? @ [ \ ] ^ _ { | } ~”), you may receive a “**No locks available**” error message and the share will not mount under&nbsp;**/home**. You will also receive a “**No locks available**” or similar&nbsp;**“Host is down”**&nbsp;error if the password is wrong or missing.

I&#8217;ve encountered the &#8222;No locks available&#8220; today and had an error in my password which blocked the auto mounter from opening the folder.