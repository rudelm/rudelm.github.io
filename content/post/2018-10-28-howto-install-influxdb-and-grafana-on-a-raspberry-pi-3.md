---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2018-10-28T18:48:54Z"
guid: http://centurio.net/?p=3198
id: 3198
image: /wp-content/uploads/2018/07/GrafanaFeinstaub-825x510.png
tags:
- Grafana
- InfluxDB
title: Howto install InfluxDB and Grafana on a Raspberry Pi 3
url: /2018/10/28/howto-install-influxdb-and-grafana-on-a-raspberry-pi-3/
---
Inspired by a friend I've decided to install [InfluxDB](https://github.com/influxdata/influxdb) and [Grafana](https://grafana.com/) on my Raspberry Pi 3. InfluxDB is a database optimized for storing time related data like measurements of my recently installed particle sensor. Grafana is used to create beautiful graphs to display the stored data.

# The InfluxDB installation can be done in a few simple steps:

<pre class="lang:sh decode:true " title="InfluxDB installation on Raspbian">curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -

echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update

sudo apt install influxdb  

sudo systemctl enable influxdb

sudo systemctl start influxdb 

influx

CREATE DATABASE topics</pre>

This will install the InfluxDB without a user and any rights. You can read up further on that [topic](https://docs.influxdata.com/influxdb/v1.5/query_language/authentication_and_authorization/). Ideally you should setup an user for authentication but since some IoT devices do not support this I'm not going to explain it here.

# The Grafana installation is similar simple:

Please make sure that you'll get the most current version from [github](https://github.com/fg2it/grafana-on-raspberry/releases) and replace it in the wget command:

<pre class="lang:sh decode:true " title="Grafana installation">wget https://github.com/fg2it/grafana-on-raspberry/releases/download/v5.1.4/grafana_5.1.4_armhf.deb

sudo dpkg -i grafana_5.1.4_armhf.deb

sudo systemctl enable grafana-server 

sudo systemctl start grafana-server</pre>

# First login to Grafana:

Now you're ready to configure Grafana. Go to http://<ip-of-grafana-machine>:3000 and setup a new username and password for the webinterface. The default is admin/admin

# Configure InfluxDB as datasource in Grafana:

You need to configure a datasource under http://<ip-of-grafana-machine>:3000/datasources

Enter as name the name of the database you've created earlier. In this case it was topic.

The type of the database is InfluxDB.

The HTTP connection URL is http://localhost:8086

Hit Save & Test, once you've configured everything to your liking. The connection to the database should work now.