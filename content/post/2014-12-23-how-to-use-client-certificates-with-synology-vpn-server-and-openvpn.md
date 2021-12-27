---
author: Centurio
categories:
- Linux
- NAS
- Security
date: "2014-12-23T17:39:01Z"
guid: http://centurio.net/?p=2167
id: 2167
tags:
- DiskStation
- OpenVPN
- Synology
title: How to use client certificates with Synology VPN Server and OpenVPN
url: /2014/12/23/how-to-use-client-certificates-with-synology-vpn-server-and-openvpn/
---
The holidays are near and I want to have access to my files on my Synology NAS, while I&#8217;m visiting my family. That&#8217;s why I&#8217;m showing you today how to configure the official Synology VPN server to use OpenVPN with client certificates instead of username/password.

&nbsp;

# 1. Start with a custom root CA

First of all you need your own self-signed root CA. A useful tool is [XCA](http://xca.sourceforge.net/) but you can also do this from the terminal.

# 2. Create a certificate for your DiskStation

Create a new Certificate for your DiskStation. Be aware to use the assigned DNS name, otherwise your browser will complain when you try to connect to the web interface of the DiskStation.

# 3. Configure the DiskStation to use the server certificate

I&#8217;m using DSM 5. There&#8217;s a nice new Security setting in the system settings. You can define and upload a certificate there:

<a href="http://centurio.net/wp-content/uploads/2014/12/ImportCertificate.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2168" src="http://centurio.net/wp-content/uploads/2014/12/ImportCertificate-300x181.png" alt="Import Certificate" width="300" height="181" srcset="https://centurio.net/wp-content/uploads/2014/12/ImportCertificate-300x181.png 300w, https://centurio.net/wp-content/uploads/2014/12/ImportCertificate-800x483.png 800w, https://centurio.net/wp-content/uploads/2014/12/ImportCertificate-35x21.png 35w, https://centurio.net/wp-content/uploads/2014/12/ImportCertificate.png 853w" sizes="(max-width: 300px) 100vw, 300px" /></a>The Private Key and Certificate fields are straight forward. However, the intermediate certificate is the tricky part I forgot. This is the certificate of your self signed root CA. Only with this additional certifacte the trust chain is complete.

# 4. Trusting the root CA

The next step depends on your computers OS. I&#8217;m using Mac OS where I can easily add the root CA certificate as an always trusted certificate.

# 5. Reload the web interface of your DiskStation

After you&#8217;ve set the certificate, the web interface should have been reloaded. Eventually you&#8217;ve been warned by your browser about a security issue (you did not trusted your root CA, therefore the web page was untrusted). After a reload and the instructions from step 4, this warning should go away. If you take a look at the certificate tab of the DiskStation&#8217;s security setting, you will see that your new server certificate is active.

# 6. Install the VPN Server

Install the VPN Server from Synology&#8217;s Package Center. Its configuration is done from the start menu.

# 7. Configure the VPN Server

Enable OpenVPN from the Settings of the VPN Server. For more details [see Synology&#8217;s instructions](https://www.synology.com/en-us/knowledgebase/tutorials/459#t3.2).

# 8. Connect via SSH to your DiskStation

Disable user authentication on the DiskStation and enable the certificate based authentication (code taken from this wiki) in this file: /usr/syno/etc/packages/VPNCenter/openvpn/openvpn.conf

<pre class="lang:sh decode:true ">#ca /var/packages/VPNCenter/target/etc/openvpn/keys/ca.crt
ca /volume1/myCA/demoCA/my-ca.crt
#cert /var/packages/VPNCenter/target/etc/openvpn/keys/server.crt
cert /volume1/myCA/syn.crt
#key /var/packages/VPNCenter/target/etc/openvpn/keys/server.key
key /volume1/myCA/syn.key

#you can enable this line temporary to view log with "tail -f -n 100 /var/log/openvpn.log":
#log-append /var/log/openvpn.log

#plugin /var/packages/VPNCenter/target/lib/radiusplugin.so /var/packages/VPNCenter/target/etc/openvpn/radiusplugin.cnf
#client-cert-not-required
#username-as-common-name

#added
user nobody
group nobody
#added</pre>

&nbsp;

# 9. Configure your client

I&#8217;m only using iOS devices and Macs. Therefore this is again a little biased 🙂 The installation of the clients for Mac and Windows is explained [on Synology&#8217;s page](https://www.synology.com/en-us/knowledgebase/tutorials/592#t4.2). iOS is explained on [this page](http://www.proenz.de/?page_id=898) (only in german but with screenshots). The initial configuration can be downloaded from the OpenVPN settings page from the DiskStation web interface. The extracted zip file contains the servers official certificates but needs to be modified to add support for the client certificates. Text is taken again from same wiki as above.

<pre class="lang:sh decode:true ">#ca ca.crt

#added
dh dh1024.pem
ca my-ca.crt
cert my.crt
key my.key
verb 3
#added

#auth-user-pass</pre>

&nbsp;

The DiffieHellmann Parameters (dh) can also be created with XCA. I would recommend 2048, since 4096 takes ages to generate.

# 10. Give it a try

Now you can test your VPN connection on your devices. It should not ask for a password, instead it should use the my.crt and my.key you&#8217;ve set in the configuration.