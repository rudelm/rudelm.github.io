---
author: Centurio
categories:
- Home Automation
- Linux
date: "2019-12-16T20:40:30Z"
guid: http://centurio.net/?p=3300
id: 3300
tags:
- Docker
- Mosquitto
- mqtt
- Synology
title: Configure Mosquitto mqtt broker  user authentication in Docker running on Synology
  NAS

---
## Introduction
Today I've tried to enable user authentication for my Mosquitto mqtt broker running in a Docker container on my Synology NAS.

### Synology folder structure
Here's my shared folder for use with docker, its under /volume1/docker:

```
mqtt
├── data
├── log
│   └── mosquitto.log
├── mosquitto.conf
└── mosquitto.passwd
```

### Permissions
The mqtt folder needs to be accessible by the docker process running in the container, e.g. by using:

```
sudo chown -R 1883:1883 mqtt/
```

### Configuration
The content of my used docker-compose.yml:

```
version: '3'
services:
  mosquitto:
    hostname: mosquitto
    image: eclipse-mosquitto:latest
    restart: always
    volumes:
      - /volume1/docker/mqtt/mosquitto.conf:/mosquitto/config/mosquitto.conf:ro
      - /volume1/docker/mqtt/mosquitto.passwd:/mosquitto/config/mosquitto.passwd
      - /volume1/docker/mqtt/log/mosquitto.log:/mosquitto/log/mosquitto.log
      - /volume1/docker/mqtt/data:/mosquitto/data
    ports:
      - "1883:1883"

```

The mapped files in the volume section need to be present, otherise docker will complain during startup of the container.

Make also sure that you're writing mosquitto with double t. I've forgotten this and used only one t, wondering why nothing was working the way I've expected it.

Here's the content of my mosquitto.conf:

```
pid_file /var/run/mosquitto.pid

persistence true
persistence_location /mosquitto/data/

log_dest file /mosquitto/log/mosquitto.log
log_dest stdout

password_file /mosquitto/config/mosquitto.passwd
allow_anonymous false
```

### Setting up accounts
You can setup the mosquitto.passwd using the docker container and/or an installation of mosquitto, so that you can use the mosquitto_passwd tool.

```
mosquitto_passwd -c /mosquitto/config/mosquitto.passwd  <username>
```

It will ask you twice for the password for the username. If you want to setup additional users, you should omit the -c parameter, so that the existing file won't be overwritten.

The  "allow_anonymous false" line will disable anonymous authentication to the broker.

You can now SSH to your Synology and start the docker container using the docker-compose file:

```
docker-compose -f docker-compose.yml up -d
```

This will look for the docker-compose.yml in the current folder and will execute docker in daemon mode. It will restart automatically when your Synology is restarting (e.g. after system updates).