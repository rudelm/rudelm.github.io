---
author: Centurio
title: "Setup Windows 11 Without Microsoft Account"
date: 2026-03-22T21:08:18+01:00
categories:
 - Windows
tags:
 - Windows 11
---
## Introduction
I've recently helped someone to reset their Windows 11 Notetbooks to a fresh state. What I wanted to avoid at all cost is the requirement of a Microsoft Account. This might have been useful if you're relying on some online features or if, like me, you're upgrading from Windows 7 and never paid for the upgrades. In any case I wanted to write down the procedure, even when it probably won't last long and will be [patched out](https://blogs.windows.com/windows-insider/2025/10/06/announcing-windows-11-insider-preview-build-26220-6772-dev-channel/#:~:text=Local%2Donly%20commands,is%20setup%20correctly) in the future.

## The how
There are several good instructions (only in German) that I've used:
 * [Deskmodder.de](https://www.deskmodder.de/wiki/index.php?title=Windows_11_mit_einem_lokalen_oder_Microsoft_Konto_installieren)
 * [Borncity.com](https://borncity.com/win/2025/10/09/windows-11-setup-microsoft-will-block-the-creation-of-local-accounts-in-the-future/) - this one is available in english

During the initial Windows 11 setup, you'll come to a step in the wizard where you're asked to select your Country. Disconnect the PC from any network and press `Shift` and `F10`. This starts the command prompt. Enter now:

```powershell
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\OOBE /v BypassNRO /t REG_DWORD /d 1 /f
```

Wait for a confirmation, then use the command `shutdown /r /t 0` and reboot. After the reboot, you should be able to create a local user.

## Conclusion
It will certainly be different next time I'll have to setup a Windows machine, but at least it will give me a working starting point, at least for March 2026.