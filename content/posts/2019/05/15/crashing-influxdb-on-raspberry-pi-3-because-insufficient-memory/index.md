---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2019-05-15T22:32:02Z"
guid: http://centurio.net/?p=3265
id: 3265
tags:
- InfluxDB
title: Crashing influxdb on Raspberry Pi 3+ because insufficient memory

---
## Introduction
A few days ago I've noticed that my influxdb installation wasn't working properly. The server was crashing constantly.

### Checking the logs
I've checked the logs using

`sudo journalctl -u influxdb -b`

and found this

```
May 12 23:12:18 pi3plus influxd[30173]: ts=2019-05-12T21:12:18.440902Z lvl=info msg="Opened file" log_id=0FNU47~W000 engine=tsm1 service=filestore path=/mnt/databases/influxdb/data/_internal/monitor/342/000000020-000000002.tsm id=0 duration=14
May 12 23:12:18 pi3plus influxd[30173]: runtime: out of memory: cannot allocate 2121015296-byte block (16056320 in use)
May 12 23:12:18 pi3plus influxd[30173]: fatal error: out of memory
May 12 23:12:18 pi3plus influxd[30173]: runtime stack:
May 12 23:12:18 pi3plus influxd[30173]: runtime.throw(0xbc70be, 0xd)
May 12 23:12:18 pi3plus influxd[30173]:         /usr/local/go/src/runtime/panic.go:608 +0x5c
May 12 23:12:18 pi3plus influxd[30173]: runtime.largeAlloc(0x7e6c15dd, 0x60101, 0x76f91a20)
May 12 23:12:18 pi3plus influxd[30173]:         /usr/local/go/src/runtime/malloc.go:1021 +0x120
May 12 23:12:18 pi3plus influxd[30173]: runtime.mallocgc.func1()
May 12 23:12:18 pi3plus influxd[30173]:         /usr/local/go/src/runtime/malloc.go:914 +0x38
May 12 23:12:18 pi3plus influxd[30173]: runtime.systemstack(0x1c4e3c0)
May 12 23:12:18 pi3plus influxd[30173]:         /usr/local/go/src/runtime/asm_arm.s:354 +0x84
May 12 23:12:18 pi3plus influxd[30173]: runtime.mstart()
May 12 23:12:18 pi3plus influxd[30173]:         /usr/local/go/src/runtime/proc.go:1229
May 12 23:12:18 pi3plus influxd[30173]: goroutine 27 [running]:
May 12 23:12:18 pi3plus influxd[30173]: runtime.systemstack_switch()
May 12 23:12:18 pi3plus systemd[1]: influxdb.service: Main process exited, code=exited, status=2/INVALIDARGUMENT
May 12 23:12:18 pi3plus systemd[1]: influxdb.service: Unit entered failed state.
May 12 23:12:18 pi3plus systemd[1]: influxdb.service: Failed with result 'exit-code'.

```

### Analysis
This happened because I've recently added statistics from my FritzBox with regards to my DSL line speed. The statistics have a high cadence, which means that many entries are created in influxdb in a short amount of time. Influxdb tries to create an index in RAM for these entries and is overwhelmed by the mass of data.

Therefore, I stopped the service with

`sudo systemctl stop influxdb`

and followed the suggestion from the [upgrade instructions](https://docs.influxdata.com/influxdb/v1.7/administration/upgrading/) to use the [influx_inspect](https://docs.influxdata.com/influxdb/v1.7/tools/influx_inspect/#buildtsi) tool.

I've executed influx_inspect as sudo and changed the permissions of my DB content folter later on with

`chown -R influxdb:influxdb <folder>`

This command may take a while to complete, depending on the size of your DB.

Once it is finished you can restart influxdb with

`sudo systemctl start influxdb`

### Conclusion
Your server should now be stable again. The index is now disk based instead of being memory based, which could cause troubles on the limited resources of the Raspberry Pi.