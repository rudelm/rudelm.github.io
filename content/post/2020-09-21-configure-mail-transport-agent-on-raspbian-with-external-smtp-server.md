---
author: Centurio
categories:
- Internet und co
- Linux
- Raspberry Pi
date: "2020-09-21T20:40:14Z"
guid: https://centurio.net/?p=3352
id: 3352
tags:
- Mail
title: Configure mail transport agent on Raspbian with external SMTP server
url: /2020/09/21/configure-mail-transport-agent-on-raspbian-with-external-smtp-server/
---
I want to get email notifications for actions on my Raspberry Pi using Raspbian. You could setup a separate mail server for that action but that seems to be a little bit overkill.

[msmtp](https://marlam.de/msmtp/) is a mail transfer agent which uses a configured smtp server for email transfer. This allows you to send emails via a configured smtp server (in my case from my webspace provider [All-Inkl.com](https://all-inkl.com/PA13DF412578D) - by [creating a new account using this link you&#8217;ll support the costs for running this blog](https://all-inkl.com/partnerprogramm/provision/)).

Upgrade your raspbian:

<pre class="wp-block-code"><code>sudo apt-get update && sudo apt-get upgrade</code></pre>

Install msmtp:

<pre class="wp-block-code"><code>sudo apt-get install msmtp msmtp-mta mailutils</code></pre>

Get the location of the configuration files:

<pre class="wp-block-code"><code>&gt; msmtp --version
msmtp version 1.6.6
Platform: arm-unknown-linux-gnueabihf
TLS/SSL library: GnuTLS
Authentication library: GNU SASL
Supported authentication methods:
plain scram-sha-1 external gssapi cram-md5 digest-md5 login ntlm
IDN support: enabled
NLS: enabled, LOCALEDIR is /usr/share/locale
Keyring support: none
System configuration file name: /etc/msmtprc
User configuration file name: /home/pi/.msmtprc

Copyright (C) 2016 Martin Lambers and others.
This is free software.  You may redistribute copies of it under the terms of
the GNU General Public License &lt;http://www.gnu.org/licenses/gpl.html&gt;.
There is NO WARRANTY, to the extent permitted by law.</code></pre>

Configure the system configuration:

<pre class="wp-block-code"><code>sudo vi /etc/msmtprc</code></pre>

The content of my configuration file (note the necessary changes for servers and email addresses):

<pre class="wp-block-code"><code># Set default values for all following accounts.
defaults

# Use the mail submission port 587 instead of the SMTP port 25.
port 465

# Always use TLS.
tls on
tls_starttls off

# Set a list of trusted CAs for TLS. The default is to use system settings, but
# you can select your own file.
tls_trust_file /etc/ssl/certs/ca-certificates.crt

# If you select your own file, you should also use the tls_crl_file command to
# check for revoked certificates, but unfortunately getting revocation lists and
# keeping them up to date is not straightforward.
#tls_crl_file ~/.tls-crls

# Mail account
# TODO: Use the users username, e.g. root for system and pi for your raspbian user
account root

# Host name of the SMTP server
# TODO: Use the host of your own mail account
host &lt;your Username provided by KAS>.kasserver.com

# As an alternative to tls_trust_file/tls_crl_file, you can use tls_fingerprint
# to pin a single certificate. You have to update the fingerprint when the
# server certificate changes, but an attacker cannot trick you into accepting
# a fraudulent certificate. Get the fingerprint with
# $ msmtp --serverinfo --tls --tls-certcheck=off --host=smtp.freemail.example
#tls_fingerprint 00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33

# Envelope-from address
# TODO: Use your own mail address
from user@domain.name

# Authentication. The password is given using one of five methods, see below.
auth on

# TODO: Use your own user name fpr the mail account
user &lt;The username of the email account you use for sending emails>

# Password method 1: Add the password to the system keyring, and let msmtp get
# it automatically. To set the keyring password using Gnome's libsecret:
# $ secret-tool store --label=msmtp \
#   host smtp.freemail.example \
#   service smtp \
#   user joe.smith

# Password method 2: Store the password in an encrypted file, and tell msmtp
# which command to use to decrypt it. This is usually used with GnuPG, as in
# this example. Usually gpg-agent will ask once for the decryption password.
#passwordeval gpg2 --no-tty -q -d ~/.msmtp-password.gpg

# Password method 3: Store the password directly in this file. Usually it is not
# a good idea to store passwords in plain text files. If you do it anyway, at
# least make sure that this file can only be read by yourself.
# TODO: Use the password of your own mail account
password &lt;The password of the email account you use for sending emails>

# Password method 4: Store the password in ~/.netrc. This method is probably not
# relevant anymore.

# Password method 5: Do not specify a password. Msmtp will then prompt you for
# it. This means you need to be able to type into a terminal when msmtp runs.

# Set a default account
# TODO: Use the same account you've configured under account, e.g. root or pi
account default: root

# Map local users to mail addresses (for crontab)
aliases /etc/aliases</code></pre>

This file contains a username and password. Therefore limit its access to only root:

<pre class="wp-block-code"><code>sudo chmod 600 /etc/msmtprc</code></pre>

Duplicate the config file to ~/.msmtprc if you want to provide email configuration for your user as well. Don&#8217;t forget to update the accounts accordingly.

Now configure the recipients for your systems users by setting the recipients in /etc/aliases. Make sure, that you don&#8217;t have trailing spaces behind the email addresses:

<pre class="wp-block-code"><code>root: user@domain.name
default: user@domain.name</code></pre>

Let your computer now that msmtp should be used as replacement for sendmail by adding this content to /etc/mail.rc

<pre class="wp-block-code"><code>set sendmail="/usr/bin/msmtp -t"</code></pre>

Test your configuration by sending an email from the terminal:

<pre class="wp-block-code"><code>echo "Content of your mail" | mail -s "Subject" user@domain.name</code></pre>