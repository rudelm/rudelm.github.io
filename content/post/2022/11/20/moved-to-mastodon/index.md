---
author: Centurio
title: "Moved to Mastodon"
date: 2022-11-20T22:35:12+01:00
categories:
- Internet und co
- Blogs
tags:
- twitter
- mastodon
- hugo
---
# Introduction
Elon Musk bought twitter. This caused a mass movement to other decentralized platforms like Mastodon.
# Fallout
I've switched this blog to run on Hugo instead of Wordpress. I've got quite a few posts that use the embedded twitter view. These embedded posts now stop a clean build of Hugo. This can either be because the linked tweet wasn't found anymore. As a workaround I had to set

```yaml
ignoreErrors: ["error-remote-getjson"]
```

in my `config.yaml` to get Hugo working again. Now I have to clean up all those embedded occurences of twitter.
# Conclusion
I've moved to Mastodon instance [infosec.exchange](https://infosec.exchange/@rudelm) and like it so far. What's annoying for me is the need for me to update my blog and remove the occurences of the embedded tweets.