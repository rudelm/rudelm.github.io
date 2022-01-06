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

---
# Introduction
Today I've updated to macOS Catalina 10.15. I've tried to setup zsh instead of bash and ran intro troubles with Xcode command line tools.

If I run

```
xcode-select -p
/Library/Developer/CommandLineTools
```

I'm seeing my previous installation in /Library/Developer/CommandLineTools. However, if I run

```
xcode-select --install
```

I'm seeing the installer which tries to fetch the latest Xcode command line tools. However, it always fails with

```
Unable to Download App. "Xcode" could not be installed. Please try again later.
```

I don't intend to install the large Xcode from the appstore. So I've tried to delete the existing installation of the command line tools with

```
sudo rm -rf /Library/Developer
```

but the problem is still present.

## Download manually

Many people suggest to go to the developer.apple.com page and to search manually for the Xcode command line tools. I thought this wouldn't work, because I'm only seeing the Xcode command line tools for Xcode 12.

{{< img "images/XcodeCommandLineTools12.png" "Xcode Command Line Tools 12 from developer.apple.com" >}}

However, we're already at Xcode 12.1, so I thought this is the wrong download and is already outdated. But after I've installed the tools from this dmg, its working again and 

```
xcode-select --install
xcode-select: error: command line tools are already installed, use "Software Update" to install updates
```

shows a suitable error message.

## Conclusion

So lessons learned: using the latest major version of the command line tools installer seems to be sufficient.