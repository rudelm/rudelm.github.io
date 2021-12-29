---
author: Centurio
categories:
- Windows
date: "2021-07-29T21:17:05Z"
guid: https://centurio.net/?p=3464
id: 3464
tags:
- Microsoft
- Windows 10
title: How to download Windows 10/11 iso using a M1 MacBook Pro
url: /2021/07/29/how-to-download-windows-10-11-iso-using-a-m1-macbook-pro/
---
I&#8217;ve recently tried [UTM](https://mac.getutm.app) on my Apple Silicon MBP to test Windows 11. To install Windows 11, I needed a recent iso image. This blog post explains how to download the iso files for Windows 10 or 11.

Go to [UUP dump](https://uupdump.net). This page lists all available UUP files from Windows Update servers.

Search for &#8222;feature update Windows 10&#8220; or &#8222;Windows 11 Insider Preview&#8220; and select a recent version for the required architecture (e.g. x64). Click on next.

Select a language and click next.

Select an edition, like &#8222;Windows Pro&#8220; and click next.

Select Download method &#8222;Download and convert to ISO&#8220;. Check &#8222;Include updates&#8220; and click on &#8222;Create download package&#8220;.

Extract the resulting file. You&#8217;ll see three scripts:

  * Windows: `uup_download_windows.cmd`
  * Linux: `uup_download_linux.sh`
  * macOS: `uup_download_macos.sh`

Make the uup\_download\_macos.sh executable by using &#8222;chmod +x uup\_download\_macos.sh&#8220; and try to execute it.

It will probably complain about missing files. But at the same time, it offers help on what you&#8217;ll need to install using homebrew, e.g.:

<pre class="wp-block-code"><code>brew tap sidneys/homebrew
brew install aria2 cabextract wimlib cdrtools sidneys/homebrew/chntpw</code></pre>

On my M1/Apple Silicon Mac, chntpw complained about a non working SSL. I&#8217;ve found this [issue on Github](https://github.com/sidneys/homebrew-homebrew/issues/2), which has some easy installation recommendations:

<pre class="wp-block-code"><code>curl -LO https://gist.github.com/minacle/e9dedb8c17025a23a453f8f30eced3da/raw/908b944b3fe2e9f348fbe8b8800daebd87b5966c/openssl@1.0.rb
curl -LO https://gist.github.com/minacle/e9dedb8c17025a23a453f8f30eced3da/raw/908b944b3fe2e9f348fbe8b8800daebd87b5966c/chntpw.rb
brew install --formula --build-from-source ./openssl@1.0.rb
brew install --formula --build-from-source ./chntpw.rb
rm ./openssl@1.0.rb ./chntpw.rb</code></pre>

Now try to execute the uup\_download\_macos.sh script again. It will now download the requested update files and will create automatically a nice ISO file, which can be used to install Windows.

As we&#8217;re using the official Windows Server Update files, this method should be legal. There is a more detailed report available ag [win10.guru](https://win10.guru/a-peek-inside-uup-dump/) which explains, that most of the tool was developed by analyzing the network traffic of a Windows installation running updates. It&#8217;s also a good way to get the versions including the latest updates including the Insider builds. Of course there&#8217;s still [the official download page](https://www.microsoft.com/en-gb/software-download/windows10ISO) from Microsoft.