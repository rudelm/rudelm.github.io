---
author: Centurio
categories:
- Linux
- NAS
- Raspberry Pi
date: "2018-11-21T22:19:09Z"
guid: http://centurio.net/?p=3236
id: 3236
tags:
- InfluxDB
title: Configure influxDB to store its data in a different folder
url: /2018/11/21/configure-influxdb-to-store-its-data-in-a-different-folder/
---
# Introduction
The default location of the influxDB data is /var/lib/influxdb.

## Change the location
If you want to change the location, you'll need to configure three folders to be in a different place. The changes should be done in the file /etc/influxdb/influxdb.conf

```
...
[meta]
  # Where the metadata/raft database is stored
  #dir = "/var/lib/influxdb/meta"
  dir = "/mnt/databases/influxdb/meta"
...
[data]
  # The directory where the TSM storage engine stores TSM files.
  #dir = "/var/lib/influxdb/data"
  dir = "/mnt/databases/influxdb/data"

  # The directory where the TSM storage engine stores WAL files.
  #wal-dir = "/var/lib/influxdb/wal"
  wal-dir = "/mnt/databases/influxdb/wal"
```

## Storing data on NFS volume
I'm using this to store the data on a NFS share [which is mounted automatically](http://centurio.net/2018/11/21/auto-mount-nfs-shares-on-raspbian/). If you want to keep your existing data, move the existing content of /var/lib/influxdb to the new location.

Make sure, that the new location is owned by influxdb user and group.