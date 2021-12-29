---
author: Centurio
categories:
- Apple
date: "2020-10-26T21:47:26Z"
guid: https://centurio.net/?p=3401
id: 3401
tags:
- Mac OS X
- Xcode
title: Fixing Xcode command line tools after upgrade to macOS Catalina 10.15
url: /2020/10/26/fixing-xcode-command-line-tools-after-upgrade-to-macos-catalina-10-15/
---
Today I&#8217;ve updated to macOS Catalina 10.15. I&#8217;ve tried to setup zsh instead of bash and ran intro troubles with Xcode command line tools.

If I run

```
xcode-select -p
/Library/Developer/CommandLineTools
```

I&#8217;m seeing my previous installation in /Library/Developer/CommandLineTools. However, if I run

```
xcode-select --install
```

I&#8217;m seeing the installer which tries to fetch the latest Xcode command line tools. However, it always fails with

```
Unable to Download App. "Xcode" could not be installed. Please try again later.
```

I don&#8217;t intend to install the large Xcode from the appstore. So I&#8217;ve tried to delete the existing installation of the command line tools with

```
sudo rm -rf /Library/Developer
```

but the problem is still present.

Many people suggest to go to the developer.apple.com page and to search manually for the Xcode command line tools. I thought this wouldn&#8217;t work, because I&#8217;m only seeing the Xcode command line tools for Xcode 12.<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="945" src="https://centurio.net/wp-content/uploads/2020/10/XcodeCommandLineTools12-1024x945.png" alt="" class="wp-image-3402" srcset="https://centurio.net/wp-content/uploads/2020/10/XcodeCommandLineTools12-1024x945.png 1024w, https://centurio.net/wp-content/uploads/2020/10/XcodeCommandLineTools12-300x277.png 300w, https://centurio.net/wp-content/uploads/2020/10/XcodeCommandLineTools12-768x709.png 768w, https://centurio.net/wp-content/uploads/2020/10/XcodeCommandLineTools12.png 1033w" sizes="(max-width: 1024px) 100vw, 1024px" /> </figure> 

However, we&#8217;re already at Xcode 12.1, so I thought this is the wrong download and is already outdated. But after I&#8217;ve installed the tools from this dmg, its working again and 

```
xcode-select --install
xcode-select: error: command line tools are already installed, use "Software Update" to install updates
```

shows a suitable error message.

So lessons learned: using the latest major version of the command line tools installer seems to be sufficient.