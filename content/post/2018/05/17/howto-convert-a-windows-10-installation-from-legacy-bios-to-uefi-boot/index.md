---
author: Centurio
categories:
- Windows
date: "2018-05-17T18:31:53Z"
glg_meta_options:
- "yes"
guid: http://centurio.net/?p=3175
id: 3175
tags:
- UEFI
- Windows 10
title: Howto convert a Windows 10 installation from legacy BIOS to UEFI boot
url: /2018/05/17/howto-convert-a-windows-10-installation-from-legacy-bios-to-uefi-boot/
---
# Introduction
I'm currently trying to build a Hackintosh. I had some troubles with bootloaders and modified BIOS, as they weren't able to detect my existing Windows 10 installation. Windows 10 was installed in legacy BIOS mode, which means you have a traditional boot layout using a Master Boot Record (MBR) instead of GPT (which is also used by Mac OS).The Windows 10 installation would be visible if I could somehow change it from MBR to GPT.

## The Problem
Normally you would do a reinstall and would create a new installation of Windows 10, but this time you would select the Installer as UEFI Installer and it would suggest to reformat the disk with GPT.

## The Solution
However, I don't want to reinstall everything so I [searched for a solution](https://www.windows-faq.de/2017/05/26/konvertieren-von-festplatten-von-mbr-auf-gpt-bei-windows-10-mit-mbr2gpt/). With one of the recent Windows 10 updates Microsoft added support for a tool called MBR2GPT. This tool can update your existing installation to GPT.

WARNING: The following assumes that you've created a working backup of your installation and that your computer supports booting via UEFI.

The necessary steps are:

  * Start your computer, so that Windows 10 is loaded.
  * Select restart and press and hold the shift key.
  * The computer will restart into Windows PE mode.
  * Select Troubleshooting, Advanced options, Command Prompt.
  * Windows will ask you to select a user name with admin rights.
  * Login with that user.
  * The Command Prompt opens and you can start the process with 
      * MBR2GPT /validate

  * If that command succeeds without errors, you can start the conversion with 
      * MBR2GPT /convert

  * You can exit the Command Prompt.
  * Reboot your computer.
  * It should boot from the found GPT partition scheme and should present you the Windows boot screen.

 
