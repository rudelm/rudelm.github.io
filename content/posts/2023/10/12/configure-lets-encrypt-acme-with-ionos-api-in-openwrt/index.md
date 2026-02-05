---
author: Centurio
title: "Configure Lets Encrypt Acme With Ionos Api in Openwrt"
date: 2023-10-12T22:53:32+02:00
categories:
- Linux
- Raspberry Pi
tags:
- OpenWRT
- Lets Encrypt
---
# Introduction
So I've got a new domain I want to use for all my local network stuff. I've used XCA to manage my own CA and got fed up by managing certs. Now I want to use Let's encrypt certificates with DNS validation, using the API provided by Ionos for managing DNS entries. My OpenWRT router should get its own certificate.

# Installation
Connect to your OpenWRT and install these packages:

```bash
opkg update
opkg install acme acme-dnsapi luci-app-acme luci-i18n-acme-en
```

# Create Ionos API credentials
See [this documentation](https://developer.hosting.ionos.de/docs/getstarted#createKey) on how to create a new API key. I've created additonally a subdomain `local` which I'll be using for all my local network stuff. I assume you'll need to have the subdomain already configured in Ionos before you'll request any certificates for subdomains.

# Configure ACME on OpenWRT
Open the LuCi UI of your OpenWRT installation. This is normally under Services, ACME certs. Keep the State directory to `/etc/acme` and add an account email that receives any messages from Let's encrypt.

## General Settings tab
Add a new certificate. In the following Popup configure the domain names under which your machine should be reachable with a valid cert.

Set Key size to `ECC 384 bits`.

Select `Use for uhttpd`, so that LuCi will use the certificate automatically.

Check `Enabled`.

## Challende Validation tab
Select Validation method `DNS`. This will offer you more options specifically for the validation via DNS entries and APIs. The DNS API [for Ionos](https://github.com/acmesh-official/acme.sh/wiki/dnsapi2#dns_ionos) is `dns_ionos`.

Now we'll add the Ionos API credentials we've configured earlier. Use for PREFIX and SECRET to separate entries in this format `IONOS_PREFIX=<your value>` and `IONOS_SECRET=<your value>`. Click on `+` for each entry to add new the variable.

We don't need Challenge Alias or Domain Alias, since we're using a DNS API.

## Testing if everything works
Click now on `Save` to close the popup. Click on `Save & Apply` and let's see if everything is working as expected. Go to `Status`, `System Log` and check any acme related entries. You should see something like this:

```
Thu Oct 12 23:13:55 2023 daemon.info acme: Using dns mode
Thu Oct 12 23:13:55 2023 daemon.err run-acme[23037]: acme: Using dns mode
...
Thu Oct 12 23:14:03 2023 daemon.info run-acme[23037]: The txt record is added: Success.
...
Thu Oct 12 23:14:24 2023 daemon.info run-acme[23037]: Pending, The CA is processing your order, please just wait. (1/30)
Thu Oct 12 23:14:27 2023 daemon.info run-acme[23037]: Success
Thu Oct 12 23:14:27 2023 daemon.info run-acme[23037]: Removing DNS records.
...
Thu Oct 12 23:14:31 2023 daemon.info run-acme[23037]: Cert success.
Thu Oct 12 23:14:31 2023 daemon.info run-acme[23037]: -----BEGIN CERTIFICATE-----
...
```

This looks promosing. Reload your browser Window and it should show the right certificate being used and signed by Let's encrypt.

# Conclusion
Wow, this was quick and painless. ACME was able to communicate with Ionos and set up all necessary DNS entries for validatoin. I'm a happy Let's encrypt certificate user now. Only downside of this approach is, that [I cannot create an ASN for the OpenWRT internal IP](https://community.letsencrypt.org/t/certificates-for-hosts-on-private-networks/174), but that's ok.