---
author: Centurio
categories:
- Home Automation
date: "2019-11-21T19:47:16Z"
guid: http://centurio.net/?p=3294
id: 3294
tags:
- OpenHAB
- Raspbian
title: Creating a backup of an existing OpenHAB installation

---
# Introduction
I'm about to try an update of my existing OpenHAB installation. Right now I've got a few things in a working state and in case I destroy anything I want to have a working backup. 

## Creating a Backup
Luckily, there's an integrated backup script on my 2.4.0 installation I can use. I just need to install the zip package first on my Raspbian using

```
sudo apt-get install zip
```

Now I can run a backup using

```
sudo $OPENHAB_RUNTIME/bin/backup

#########################################
       openHAB 2.x.x backup script
#########################################

Using '/etc/openhab2' as conf folder...
Using '/var/lib/openhab2' as userdata folder...
Using '/usr/share/openhab2/runtime' as runtime folder...
Using '/var/lib/openhab2/backups' as backup folder...
Writing to '/var/lib/openhab2/backups/openhab2-backup-19_11_21-19_24_30.zip'...
Making Temporary Directory if it is not already there
Using /tmp/openhab2/backup as TempDir
Copying configuration to temporary folder...
Removing unnecessary files...
Backup Directory is inside userdata, not including in this backup!
Zipping folder...
Removing temporary files...
Success! Backup made in /var/lib/openhab2/backups/openhab2-backup-19_11_21-19_24_30.zip
```

## Conclusion
The backup includes the installed plugins as well as the used configuration. Quite easy and fun to use!