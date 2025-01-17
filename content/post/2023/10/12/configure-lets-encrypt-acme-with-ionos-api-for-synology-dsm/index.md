---
author: Centurio
title: "Configure Lets Encrypt Acme With Ionos Api for Synology DSM"
date: 2023-10-12T23:33:40+02:00
categories:
- Linux
tags:
- Synology
- Lets Encrypt
---
# Introduction
I've (just setup]({{< ref "/post/2023/10/12/configure-lets-encrypt-acme-with-ionos-api-in-openwrt" >}}) a Let's encrypt certificate for my OpenWRT router. I would like to do the same for my Synology NAS. However, this one is a bit more complex, since I'm running a lot of docker container on that machine and also use the reverse proxy feature. So I'll need a wildcard certificate. Unfortunately, DSM doesn't support Let's encrypt certificates using DNS validation, so I'll have to do things manually. Luckily (some people](https://www.christosgeo.com/2022/02/03/renew-lets-encrypt-certificates-on-synology-using-acme-sh/) already experimented with this problem and documented them.

# Create Ionos API credentials
See (this documentation](https://developer.hosting.ionos.de/docs/getstarted#createKey) on how to create a new API key. I've created additonally a subdomain `local` which I'll be using for all my local network stuff. I assume you'll need to have the subdomain already configured in Ionos before you'll request any certificates for subdomains.

# Preparations
The suggestion is to run the ACME script inside a docker container. Additionally a separate DSM admin user should be used for managing the certificate renewal process. The user must be an admin, but can be denied access to all DSM Applications. You'll have to login once for this user, to complete the 2FA setup.

# ACME container
We'll run the ACME script inside a docker container. So assuming you've already got docker installed on your DSM and setup.
## account.conf
Create a new folder and put the following content into the file `account.conf`. I've put mine under `/volume1/docker/acme`

```bash
export IONOS_PREFIX="yourusername"
export IONOS_SECRET="yourpassword"
export SYNO_Username="yoursynologyadminuser"
export SYNO_Password="yoursynologyadminuserpassword"
export SYNO_Certificate=""
export SYNO_Scheme="https"
export SYNO_Port="5001"
export SYNO_Hostname="yoursynologyFQDN"
export SYNO_Create=1
```

Change the values to your needs. The `SYNO_Username` and password are of the account you've created earlier. The `IONOS_` parameters are from the API credential creation of Ionos.

## The Container
I'm using Portainer for most of my docker stuff. But since I'm following (these instructions](https://www.christosgeo.com/2022/02/03/renew-lets-encrypt-certificates-on-synology-using-acme-sh/) I'll be configuring this container via the DSM console.

Enabe automatic restarts and give it a simple name like acme.

Connect to the Terminal like it is described. Change the default CA to letsencrypt:

`acme.sh --set-default-ca --server letsencrypt`

Now comes the interesting part, issueing a new certificate:

`acme.sh --issue --dns dns_ionos -d yourdomain -d *.yourdomain`

Note the double `-d` parameters. We want a wildcard certificate for any subdomains and also an ASN for the domain of the DSM as a host. If the execution is successful, you'll have new signed certificates in `/volume1/docker/acme`.

Now we'll deploy them to the Synology:

`acme.sh --deploy -d yourdomain -d *.yourdomain --deploy-hook synology_dsm --insecure`

I had problems with my existing certs which weren't trusted by the docker container, so I had to disable verification with --insecure. After execution I've got an error that the restart of the HTTP services failed:

```
[Fri Oct 13 00:12:28 UTC 2023] Getting certificates in Synology DSM              
[Fri Oct 13 00:12:28 UTC 2023] Generate form POST request                        
[Fri Oct 13 00:12:28 UTC 2023] Upload certificate to the Synology DSM            
[Fri Oct 13 00:12:29 UTC 2023] Restarting HTTP services failed                   
[Fri Oct 13 00:12:29 UTC 2023] Success   
```

The list of certificates now show the uploaded certificate from lets encrypt, but its not in use anywhere inside the DSM. According to (this wiki](https://github.com/acmesh-official/acme.sh/wiki/deployhooks#20-deploy-the-certificate-to-synology-dsm), it must be assigned manually:

```
Afterwards, the certificate should show up inside Control Panel -> Security -> Certificates & can be assigned to specific services or set as the default certificate.
```
 
When I assign it manually, it will trigger a restart of the webserver automatically. The new certificate is now in use

# Conclusion
After some minor problems with the `synology_dsm` deploy hook, I've got it all running. It will be interesting to see how things will end up in 90 days, when the certificate expire. Ideally the docker container will handle the renewal process automatically. In combination with the deploy hook, the DSM should pretty much maintenance free.

# Update 04/11/2024
I've just witnessed another expired certificate without my knowing. According to the acme container, it should be renewed only in a month, but is already expired for 2 days:

```bash
2024/04/11 00:49:03	stdout Wed Apr 10 22:49:03 UTC 2024 Skip, Next renewal time is: 2024-05-11T22:49:51Z
```

But according to the logs, acme already tried to renew a certificate in March 2024:

```bash
2024/03/13 23:49:51	stdout Wed Mar 13 22:49:51 UTC 2024 Cert success.
```

It failed to update the certificate in the DSM again:

```bash
2024/03/13 23:49:59	stdout Wed Mar 13 22:49:59 UTC 2024] Unable to authenticate to https://myds:5001 - check your username & password.
```

I've tried again to configure the deploy hook but I couldn't get past the authentication:

```bash
[Thu Apr 11 22:18:30 UTC 2024] Session ID
[Thu Apr 11 22:18:30 UTC 2024] SynoToken
[Thu Apr 11 22:18:30 UTC 2024] Unable to authenticate to https://myds:5001 - check your username & password.
[Thu Apr 11 22:18:30 UTC 2024] If two-factor authentication is enabled for the user:
[Thu Apr 11 22:18:30 UTC 2024] - set SYNO_Device_Name then input *correct* OTP-code manually
[Thu Apr 11 22:18:30 UTC 2024] - get & set SYNO_Device_ID via your browser cookies
[Thu Apr 11 22:18:30 UTC 2024] Error deploy for domain:myds
[Thu Apr 11 22:18:30 UTC 2024] Deploy error.
```

I've had this problems before and looking at [the github issue](https://github.com/acmesh-official/acme.sh/issues/2727), it's often causing problems. In its current state, it's too fragile so I've selected manually the certificate and replaced the expired one. Guess I'll rather check for any renewal emails or other notification and have to do this manually. There's also the possibility to run acme natively on the DSM to avoid having authentication problems but I did not give it a try yet.