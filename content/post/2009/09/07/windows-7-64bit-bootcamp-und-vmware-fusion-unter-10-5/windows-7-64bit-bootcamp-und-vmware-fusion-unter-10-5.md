---
author: Centurio
categories:
- Apple
- Windows
date: "2009-09-07T19:02:29Z"
guid: http://centurio.net/?p=1168
id: 1168
tags:
- BootCamp
- VMWare
title: Windows 7 64Bit BootCamp und VMWare Fusion unter 10.5
url: /2009/09/07/windows-7-64bit-bootcamp-und-vmware-fusion-unter-10-5/
---
Ich habe heute ja erst gemerkt, dass ich Probleme bekommen könnte, wenn ich Fusion starte und auf meine bereits eingerichtete BootCamp Maschine zugreifen möchte: Der Grund für die Probleme war, dass ich die bestehende Windows XP BootCamp Konfiguration in Fusion übernommen hatte (irgendwie ließ sich die VM nämlich nicht aus Fusion heraus löschen, und das Konfigurieren auf Vista 64-Bit brachte auch keine Besserung).

Man muss erst diese BootCamp Konfiguration loswerden und löschen, danach erst beginnt VMWare erneut BootCamp zu konfigurieren für die Nutzung mit Fusion.

Dazu muss man also nur ~/Library/Application Support/VMware Fusion/Virtual Machines/Boot Camp löschen. Danach kann man Fusion neu aufrufen und die neue VM Konfigurieren.

Jetzt hatte VMWare auch richtig erkannt, dass es sich um eine 64-Bit Windows Variante handelt und hat dann entsprechend die VMWare Tools installiert. Und siehe da, alles läuft wieder 🙂