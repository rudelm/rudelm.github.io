---
author: Centurio
title: "Using Github Pages With All Inkl"
date: 2023-05-06T20:51:18+02:00
categories:
- blogs
tags:
- Github
- Hugo
---
# Introduction
I've recently found [this](https://christianspecht.de/2017/02/26/dns-settings-for-github-pages-read-the-docs-with-only-one-a-record/) blog post and tried today, if I could host my hugo blog on github pages in combination with my hoster all-inkl.com. Here are the steps that I followed:

# Following the official instructions
The [gohugo.io](https://gohugo.io/hosting-and-deployment/hosting-on-github/) page offers a good instruction page on what to do. Everything was unproblematic up until the point to where I generated rudelm.github.io.

# Configure all-inkl
In KAS, you can configure DNS settings for your domain. I've had to change the A record for centurio.net to `185.199.108.153` as it is recommended [here](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). I've also added an AAAA IPv6 record to `2606:50c0:8000::153`.

You can verify that the records are set using the dig command:


```bash
dig centurio.net +noall +answer -t A

; <<>> DiG 9.10.6 <<>> centurio.net +noall +answer -t A
;; global options: +cmd
centurio.net.		7012	IN	A	185.199.108.153

dig centurio.net +noall +answer -t AAAA

; <<>> DiG 9.10.6 <<>> centurio.net +noall +answer -t AAAA
;; global options: +cmd
```

The IPv6 entry doesn't show up yet and I'll try to check this later on again. **Update**: It's now working:

```bash
dig centurio.net +noall +answer -t AAAA

; <<>> DiG 9.10.6 <<>> centurio.net +noall +answer -t AAAA
;; global options: +cmd
centurio.net.		3392	IN	AAAA	2606:50c0:8000::153
```
Don't forget to add a CNAME record for www so that it points to the github.io page, in my case rudelm.github.io.

# Configure github
Go to the settings of your personal repo and check the pages menu. Add the custom domain under which your hugo blog should be reachable. Github will then trigger an automated DNS check. This one currently fails for me:

```
Both centurio.net and its alternate name are improperly configured
Domain does not resolve to the GitHub Pages server. For more information, see documentation (NotServedByPagesError).
```

However, I've seen that github tried to request a TLS certificate in a three step process, so I assume at least something must be working.

**Update**: the DNS check is now successful.

# Conclusion
I finally don't have to upload everything again and again using ftp. This was quite error prone and inefficient. I can now blog and push it to github, and the github action will create new pages for me automatically.