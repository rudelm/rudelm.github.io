---
author: Centurio
title: "Stop Apple Music From Starting Automatically"
date: 2026-03-23T23:13:41+01:00
categories:
 - macOS
tags:
 - Apple Music
 - Qobuz
---
## Introduction
I've used to host my Music library on my NAS using [Automount](/tags/automount/). This worked quite fine. However, I'm not using those files anymore and stopped maintaining my Apple Music library, as the mount was often failing. In combination with Bluetooth speakers or other multimedia keys, I've started quite often Apple Music without a reason. [noTunes](https://github.com/tombonez/noTunes) is a small macOS app that provides better control over this behavior.

## Installation
Install it using `brew install --cask notunes` and you're done. After installation, you can start it. The menubar shows a symbol that is either crossed or not crossed. That's the status of Apple Music starting or not.

## Setting a replacement for Apple Music
With this app it is possible to define other music players as default app. You can e.g. start Qobuz this way: `defaults write digital.twisted.noTunes replacement /Applications/Qobuz.app`

## Conclusion
A small but nice app that I don't want to loose in the future, that's why I've made a short blog post about.