---
author: Centurio
categories:
- Linux
- Raspberry Pi
date: "2019-05-15T23:11:35Z"
guid: http://centurio.net/?p=3267
id: 3267
image: /wp-content/uploads/2019/05/grafana-fritzbox-dashboard-825x510.png
tags:
- Fritz!Box
- Grafana
- InfluxDB
title: Monitor Fritz!Box connection statistics with Grafana, InfluxDB and Raspberry
  Pi
url: /2019/05/15/monitor-fritzbox-connection-statistics-with-grafana-influxdb-and-raspberry-pi/
---
I&#8217;ve recently stumbled over an [article](https://www.heise.de/select/ct/2018/21/1539315226273140) in the german magazine C&#8217;T about visualisations of your Fritz!Box&#8217;s connection. The solution looked quite boring and outdated, since it used [MRTG](https://oss.oetiker.ch/mrtg/) for the graph creation.

I&#8217;ve started searching for a better solution using Grafana, InfluxDB and my Raspberry Pi and found this great blog post. I&#8217;ve [already explained](https://centurio.net/2018/10/28/howto-install-influxdb-and-grafana-on-a-raspberry-pi-3/) how to install Grafana and InfluxDB in this post, so I&#8217;ll concentrate on the Fritz!Box related parts:

Start with the installation of fritzcollectd. It is a plugin for collectd.

```
sudo apt-get install -y python-pip
sudo apt-get install -y libxml2-dev libxslt1-dev
sudo pip install fritzcollectd
```

Now create a user account in the Fritz!Box for collectd. Go to System, Fritz!Box-user and create a new user with password, who has access from internet disabled. The important part is to enable &#8222;Fritz!Box settings&#8220;.

Additionally make sure that your Fritz!Box is configured to support connection queries using UPnP. You can configure this under &#8222;Home Network > Network > Networksettings&#8220;. Select &#8222;Allow access for applications&#8220; as well as &#8222;Statusinformation using UPnP&#8220;. 

Next part is the installation and configuration of collectd:

```
sudo apt-get install -y collectd
sudo nano /etc/collectd/collectd.conf
```

Enable the python and network plugins by removing the hashtag

```
LoadPlugin python
[...]
LoadPlugin network
```

Scroll down till you&#8217;ll see the plugin configuration and configure the port and IP for collectd

```
&lt;Plugin network>
    Server "127.0.0.1" "25826"
&lt;/Plugin>
```

Enable the python plugin and configure the module with the username and password of the user you&#8217;ve created. Make also sure to use the right address.

```
&lt;Plugin python>
    Import "fritzcollectd"

    &lt;Module fritzcollectd>
        Address "fritz.box"
        Port 49000
        User "user"
        Password "password"
        Hostname "FritzBox"
        Instance "1"
        Verbose "False"
    &lt;/Module>
&lt;/Plugin>
```

Since you&#8217;ve already got a running InfluxDB, you&#8217;ll just need to enable collectd as data source:

```
sudo nano /etc/influxdb/influxdb.conf
```

Search for the [collectd] part and replace it with

```
[[collectd]]
  enabled = true
  bind-address = "127.0.0.1:25826"
  database = "collectd"
  typesdb = "/usr/share/collectd/types.db"
```

Reboot collectd and influx to activate the changes made

```
sudo systemctl restart collectd
sudo systemctl restart influxdb
```

Login to your grafana installation and configure a new datasource. Make sure to set the collectd database. If you&#8217;re using credentials for the InfluxDB, you can add them now. If you&#8217;re not using authentication you can disable the &#8222;With credentials&#8220; checkbox.<figure class="wp-block-image">

<img loading="lazy" width="782" height="866" src="http://centurio.net/wp-content/uploads/2019/05/influxdb-collectd-datasource.png" alt="" class="wp-image-3268" srcset="https://centurio.net/wp-content/uploads/2019/05/influxdb-collectd-datasource.png 782w, https://centurio.net/wp-content/uploads/2019/05/influxdb-collectd-datasource-271x300.png 271w, https://centurio.net/wp-content/uploads/2019/05/influxdb-collectd-datasource-768x850.png 768w" sizes="(max-width: 782px) 100vw, 782px" /> </figure> 

Check if your configuration is working by clicking on &#8222;Save & Test&#8220;. 

If everything worked, you can proceed to importing the Fritz!Box Dashboard from the Grafana.com dashboard. The ID is 713. Make sure to select the right InfluxDB during the import setup.

After clicking on import, you&#8217;ll should be able to see your new Dashboard. It might take a few minutes/hours until you&#8217;ve gathered enough data to properly display graphs.<figure class="wp-block-image">

<img loading="lazy" width="1024" height="634" src="http://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard-1024x634.png" alt="" class="wp-image-3269" srcset="https://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard-1024x634.png 1024w, https://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard-300x186.png 300w, https://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard-768x476.png 768w, https://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard-825x510.png 825w, https://centurio.net/wp-content/uploads/2019/05/grafana-fritzbox-dashboard.png 1586w" sizes="(max-width: 1024px) 100vw, 1024px" /> </figure> 

Be aware though that if you start gathering this much data you&#8217;ll might end up with [&#8222;insufficient memory&#8220; errors](https://centurio.net/2019/05/15/crashing-influxdb-on-raspberry-pi-3-because-insufficient-memory/). You&#8217;ll might want to tweak your InfluxDB settings accordingly.