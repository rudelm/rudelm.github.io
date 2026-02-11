---
author: Centurio
title: "1Password SSH Integration on macOS"
date: 2024-11-29T22:29:54+01:00
categories:
- Linux
- Raspberry Pi
- macOS
tags:
- linux
- 1Password
- SSH
---
## Introduction
I've recently tried to setup a Raspberry Pi for SSH. I've created a new SSH entry in 1Password and wanted to use the great 1Password SSH integration for this. Unfortunately I was unable to get it working. After many careful reads of the documentation, I've finally found a working configuration. This post should explain that setup a little bit as a personal reminder.

## The general stuff
I"ve already had my 1Password configured to support SSH keys. 1Password has [this explanation](https://developer.1password.com/docs/ssh/get-started/) which I've followed on my Mac. So the entry in 1Password was already present and [the agent](https://developer.1password.com/docs/ssh/agent/config/) was configured to search in several of my vaults for SSH keys.

Usually, an entry in my `~/.ssh/config` would look like this:

```bash
Host pi3work
	UseKeychain yes
	AddKeysToAgent yes
	HostName 192.168.123.10
	Port 22
	User pi
	IdentityFile ~/.ssh/id_ed_pi3work
```

Somehow I thought, I'll have to replace the file path for the `IdentityFile` with the reference to the entry in 1Password's private part of the SSH key. So something like `op://VaultName/EntryName/private key`. I've then tried to connect with ssh and got an error:

```bash
no such identity: op://VaultName/EntryName/private key: No such file or directory
```

## Solving the problem
The entry was clearly present in 1Password. I could even run `ssh-add -l` to list the currently known keys for the SSH agent, but something was clearly not working. After carefully rereading the documentation I've found the issue. Instead of using `IdentityFile` I've had to use this line `IdentityAgent ~/.1password/agent.sock`.

The link to the agent can be created with this command:

```bash
mkdir -p ~/.1password && ln -s ~/Library/Group\ Containers/2BUA8C4S2C.com.1password/t/agent.sock ~/.1password/agent.sock
```

## Conclusion
It was quite easy, when you'll use the right values from the documentation. But regardless of this I was sure, I've had this somehow working before using the `IdentityFile` in combination with a 1Password link. Now I've got both variants documented, in case I'll forget this again with the next SSH key not working anymore.