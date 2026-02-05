---
author: Centurio
title: "Update Acme.sh Docker Container"
date: 2025-04-27T21:01:40+02:00
categories:
- Linux
- Raspberry Pi
tags:
- linux
- acme
---
# Introduction
I'm using [Diun](https://github.com/crazy-max/diun) to be notified about outdated Docker container. Today I was notified about an outstanding update for [acme.sh](https://github.com/acmesh-official/acme.sh). I'm using acme in various variants but this container was running on my Synology, outside the management provided by [Dockge](https://github.com/louislam/dockge), so I had to update the container manually.

# Update procedure
Login to your Host via SSH and become root. Update to the latest image by using `docker pull neilpang/acme.sh`. Here's an example call from my machine:

```bash
ash-4.4# docker pull neilpang/acme.sh
Using default tag: latest
latest: Pulling from neilpang/acme.sh
f18232174bc9: Already exists
a02477d504ae: Pull complete
cdbb199096b6: Pull complete
e84b361f958b: Pull complete
d2ab1c727d8c: Pull complete
b17b2bc9b3ea: Pull complete
ec66d11b3eb8: Pull complete
166c8dec79a1: Pull complete
99b492c2aef4: Pull complete
6a45f468ca50: Pull complete
Digest: sha256:1900e9b22a4859c6e1da3bb8184d5a129d63537502f9f9053b807dc2939c1e23
Status: Downloaded newer image for neilpang/acme.sh:latest
docker.io/neilpang/acme.sh:latest
```

Now you'll have to recreate the currently running container. You can check if your container is running by using `docker ps|grep acme`. Again an example output:

```bash
ash-4.4# docker ps|grep acme
1144de4611aa   187c1f47ec28                                   "/entry.sh daemon"       15 months ago    Up 2 weeks                                                            acme
```

For the recreation you'll need to know how you'll originally started your container. I did this manually when I setup acme for the first time using [these instructions]({{< ref "/posts/2023/10/12/configure-lets-encrypt-acme-with-ionos-api-in-openwrt" >}}). My only custom modification was that I'm referencing a volume to keep my certificates.

You can now either stop, remove and recreate the container or stop, remove and recreate it in a docker-compose file. I've chosen the latter variant to spare me from future manual updates. My `docker-compose.yml` looks like this:

```yaml
services:
  acme:
    image: neilpang/acme.sh:latest
    container_name: acme
    restart: unless-stopped
    command: daemon
    volumes:
      - /volume1/docker/acme:/acme.sh
networks: {}
```

Now I can just hit update in Dockge and I'm getting my container updated.

# Conclusion
I have no idea why I did not move acme to a docker-compose file earlier. Updating it this way is way more comfortable.  But the best thing about this update is probably that I've did migrate my setup to Dockge.
