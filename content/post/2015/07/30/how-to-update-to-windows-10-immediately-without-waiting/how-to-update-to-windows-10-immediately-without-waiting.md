---
author: Centurio
categories:
- Windows
date: "2015-07-30T22:01:24Z"
guid: http://centurio.net/?p=2236
id: 2236
tags:
- PC
- Windows 10
title: How to update to Windows 10 immediately without waiting
url: /2015/07/30/how-to-update-to-windows-10-immediately-without-waiting/
---
I've reserved on my Windows 8.1 machine the Windows 10 update a few weeks ago. Since yesterday you can now officially install Windows 10 in its final version. The Microsoft update tool should notify you, when the update is ready to install.

However, Microsoft decided to deliver the update files in several waves to keep the load from their content delivery network.

If you are like me interested in getting the newest versions immediately, you'll probably checked your Windows update setting and didn't notice any new updates for you.

Yesterday Ginny Caughey recommended to just use a certain command:

{{< tweet user="gcaughey" id="626352655217106944" >}}

The recommended command is this one:

```
wuauclt.exe /updatenow
```

This command should circumvent the limitations given by Microsoft regarding your position in the update waves. However, it always ended in error messages for me, besides downloading around 2,7GB of setup files.

Today I've [read](http://www.heise.de/newsticker/meldung/Windows-10-Upgrade-Download-von-Hand-anstossen-2765187.html) that there is already [a tool available from Microsoft](https://www.microsoft.com/en-us/software-download/windows10ISO) which allows you to create a bootable installation media from a downloaded Windows 10 iso file. This tool also allows you to start the installation of Windows 10 immediately, so you don't have to wait any longer.

Right now this tool is running and updates my PC to Windows 10 🙂