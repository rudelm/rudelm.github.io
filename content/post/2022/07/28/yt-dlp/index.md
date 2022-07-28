---
author: Centurio
title: "yt-dlp - a command line youtube downloader"
date: 2022-07-28T08:44:05+02:00
categories:
- Internet und co
tags:
- Youtube
- yt-dlp
- youtube-dl
---
# Introduction
In 2021 there was a [larger discussion](https://github.blog/2020-11-16-standing-up-for-developers-youtube-dl-is-back/) about the tool youtube-dl. It is a downloader for all sorts of video content. I recently stumbled into slow downloads and searched for alternatives and found [yt-dlp](https://github.com/yt-dlp/yt-dlp/), which is a fork of youtube-dl.

# Installation
On macOS it can be installed without python hassle by using homebrew: `brew install yt-dlp/taps/yt-dlp`

# Usage
It can be used with the same parameters as youtube-dl. However, there are options missing. Its best to check the documentation for the specifics.

# Conclusion
yt-dlp works much faster when compared to youtube-dl. Its also easy to install and update (with homebrew its just `brew upgrade yt-dlp/taps/yt-dlp`).