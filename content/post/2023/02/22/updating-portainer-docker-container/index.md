---
author: Centurio
title: "Updating Portainer Docker Container"
date: 2023-02-22T20:33:06+01:00
categories:
- Linux
tags:
- Portainer
- Docker
---
# Introduction
I've recently tried [Portainer](https://www.portainer.io/) to manage all of my docker containers on my Synology NAS. A single docker-compose file caused already issues, e.g. the timeout for the `docker compose up` command had to be increased and for each small change I had to shut down all containers. With Portainer, I start a single portainer docker container and can manage all other containers through this single container.

I've started with Portainer 2.17.0 and today Portainer 2.17.1 was released. Time to upgrade my Portainer installation. But how does this work? I've already used the docker image tagged latest, which is obviously not the newest anymore.

# Update the container
I've started my installation of Portainer with this command:

```bash
docker run -d -p 9000:9000 \
    --name=portainer_ee \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /volume1/docker/portainer_ee/data:/data \
    --restart=always \
    portainer/portainer-ee:latest
```

Notice the volume where I've mounted the data. This will ensure that my data survives the following steps.

```bash
docker stop portainer_ee

docker rm portainer_ee

docker pull portainer/portainer-ee:latest
```

Now start portainer again.

# Conclusion
Updating Portainer is easy and doesn't cost much time. Already started containers stay up and have no downtime. Sweet!