---
author: Centurio
title: "Let's Encrypt certificates with Porkbun API on HomeAssistant OS"
date: 2024-12-16T20:21:40+01:00
categories:
- Linux
- Raspberry Pi
tags:
- homeassistant
---
## Introduction
I've reused one of my Raspberry Pi CM4 as a HomeAssistant server using HomeAssistant OS. To have finally TLS encryption running on this machine, I want to use Let's Encrypt certificates. The domain I'm using is managed by Porkbun and I want to use DNS validation. Last but not least I want everything as an addon managed through HomeAssistant.

## Research
I've started looking for explanations from other users and found a really [good blog post from Dustin Casto](https://theprivatesmarthome.com/how-to/enable-https-using-lets-encrypt-in-home-assistant/). He made a lot of screenshots and explained the details, so I'm trying to limit this post to mainly explaining how to use Porkbun in this constellation.

## Preparation & Setup

### Porkbun
Let's start with the configuration of Porkbun. You'll need to [create API credentials](https://kb.porkbun.com/article/190-getting-started-with-the-porkbun-api) and end up with two values:
* API Key
* Secret Key

### HomeAssistant addon
On the HomeAssistant we'll install the `Let's Encrypt` add on. Once it's configured and started, go to configuration. Enter the domain names you'll want to issue the certificate for. This domain must be managed by Porkbun. Leave the filename's as they are `privkey.pem` and `fullchain.pem` and set `dns` as Challenge.

The interesting part was now the [necessary options for configuring porkbun](https://github.com/home-assistant/addons/blob/master/letsencrypt/DOCS.md). It's not the regular configuration option I've known from [ACME](https://github.com/acmesh-official/acme.sh/wiki/dnsapi2#dns_porkbun). Use these values and adjust the key and secret to the values you've created earlier:

```bash
provider: dns-porkbun
porkbun_key: XXXXXXX
porkbun_secret: XXXXXXX
```

Click on Save and Start the add on. After a few seconds you'll see that the add on is running. If you'll check the Log tab, you'll see that the add on created a certificate for you.

### Automate renewal
This one needs a verification if it's really working, since my generated certificate did not expire yet.  Dustin used an automation to trigger the start of the addon to a given time, so it identifies the certificate expiry and replaces it with a new one. I don't know though, if its notifying HomeAssistant about the change, so that it restarts it's web server automatically.

### Use the generated certificate
You'll have to edit your `configuration.yaml` so that it uses TLS and port 443, together with the created certificate. You'll find your `privkey.pem` and `fullchain.pem` in the `/ssl` folder on HomeAssistant OS. Add these entries in your `configuration.yaml`:

```bash
# TLS with letsencrypt add-on
http:
  server_port: 443
  ssl_certificate: /ssl/fullchain.pem
  ssl_key: /ssl/privkey.pem
```

Save the file and do a system restart. Your machine will be now reachable only via TLS.

## Conclusion
There's much more to do, once this is setup. I've created an entry in Uptime Kuma to track the expiration of the TLS certifacte, just to verify if I'll run into problems with the renewal. [Other people](https://hanjo.dev/blog/use-home-assistant-to-dynamically-update-your-porkbun-dns-records) [automated their DynDNS entries](https://gist.github.com/leowinterde/fefef8d803b4810d74de26cab5433b6c) using the Porkpun credentials.

This might come in handy when using DynDNS in combination with Let's encrypt certificates. I'm still struggling to find a suitable way for connecting to my HomeAssistant installation when I'm on the road though. 