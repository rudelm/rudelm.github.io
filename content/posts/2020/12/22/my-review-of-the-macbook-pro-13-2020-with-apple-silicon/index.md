---
author: Centurio
categories:
- Apple
- Hardware
date: "2020-12-22T22:34:43Z"
guid: https://centurio.net/?p=3416
id: 3416
tags:
- Apple Silicon
- arm64
- M1
- MacBookPro
title: My Review of the MacBook Pro 13" (2020) with Apple Silicon

---
# Introduction

After careful considerations and watching a lot of YouTube videos about the new Macs with Apple Silicon hardware, I've decided to order myself a shiny new MacBook Pro 13" with 16GB RAM and 512GB SSD. I could compare it to my works MacBook Pro 16" as well as my older MacBook Pro 15" from mid 2014 and I must say, I'm really impressed.

## General Things

The hardware is just great. I like the overall form factor and its small size compared to my wife's MacBook Air 13" 2015. The MacBooks internal speaker sound reasonable, but cannot compare to the awesome sound of the MacBook Pro 16". But since I don't use the internal speaker that often, I can live with the current quality.

The temperature of the MacBook is always cold, regardless of the current workload. This means, you cannot use it anymore to warm your hands in winter but also its totally quiet, even when it has an internal fan! This is a huge plus, as I'm finally having a quiet desktop again!

Another thing I like is the instant on/wakeup. This machine feels like it is an iPad. That also affects the battery life which is just crazy and unparalleled. If you'll attach a screen it will turn on immediately. There's no fade to black first.

## M1 compatible apps

Apple Silicon is using arm64 as new architecture compared to Intel. That means all existing Intel Mac Software is run in Rosetta 2, the emulation layer for software which is only compiled for the Intel architecture. There's already a [huge list of supported software](https://isapplesiliconready.com/de/for/m1). Some [apps are not working](https://forums.macrumors.com/threads/big-sur-working-not-working-apps.2242312/) and even [Homebrew has its ongoing issues](https://github.com/Homebrew/brew/issues/7857), but [is already useable](https://soffes.blog/homebrew-on-apple-silicon).

## Software left to check at a later time

Docker preview is already available for Apple Silicon, but is not a final stable version.

LuLu Firewall for outgoing connections is currently compiled for the Intel architecture. However, there’s [already work going on in that area](https://twitter.com/patrickwardle/status/1336144373549953024?s=20) and I’m looking forward to it.

Visual Studio Code - Insiders available for Apple Silicon, but not a final stable version. Crashes since its last update and I’ve replaced it with the Intel version again.

Thunderbird is still compiled for Intel, whereby Firefox is already available for Apple Silicon.

StarCraft 2 is still compiled for Intel, whereby World of Warcraft is already available for Apple Silicon. Works in FullHD on external screen without sync on low Settings but high texture settings around 60-80 FPS.

Other Software I use but which is still compiled for Intel:

  * TextMate
  * Tunnelblick
  * Jdownloader 2
  * Spotify
  * Logitech Options

## Using Safari as new default browser

I've read somewhere that Safari is so much faster on Apple Silicon compared to Chrome, so I've decided to use Safari as my new default browser for the time being. However, as it turns out, this was [only true until Google published an Apple silicon version of Chrome](https://www.imore.com/google-chrome-sees-2x-performance-boost-apple-silicon) enabling much faster performance.

I've upgraded my 1Password license from 6 to 7. This enabled the extension in Safari again, as my previous 1Password 6 license was not supported anymore.

There's a new webfiltering extension used in Safari > 14. My Adblocker needed  updates to support this. I’m currently using [Wipr](https://giorgiocalderolla.com/index.html) from the App Store for 1,99$[]()

Wipr's looking good so far. It filters even most of the YouTube ads, leaving only from time to time a “Skip ad” but without content.

## Issues so far

### External Screen was not recognized

This is a thing I’ve witnessed on almost all my Macs I’ve used in combination with Thunderbolt docks. I’m using my Macs in Clamshell mode and only rely on wakeup by typing on external keyboard or clicking on my mouse. The Mac did not wake up and I did not have any picture visible on the screen. However, once I’ve opened the MacBook it waked instantly up and detected all external hardware including the screen.

### Internal Screen resolution is wrong

The MacBook Pro wakes up after it was connected via USB-C to an external monitor with WQHD resolution. The screen flickers a little bit and the displayed resolution doesn't fit the screen. Changing the Display options in System Settings doesn't change this behaviour and the right side of the desktop is invisible as well as the lower part. If I take a screenshot, it will show all details. Looks like [this](https://developer.apple.com/forums/thread/654876) is [a Big Sur problem](https://forums.macrumors.com/threads/m1-air-ghosting-flickering-with-external-display.2271670) with [external wide screens](https://screenrant.com/apple-m1-mac-external-display-issue-app-solution/).

### Bluetooth connectivity

This seems to be [a well known bug](https://www.reddit.com/r/macmini/comments/jye3hc/m1_mac_mini_has_bluetooth_issues/). I've connected a Magic Trackpad and it keeps on disconnecting, regardless the real distance to the MacBook Pro. You can manually disconnect, but it will try to reconnect, even when it isn't touched and will show a lot of annoying system notifications.