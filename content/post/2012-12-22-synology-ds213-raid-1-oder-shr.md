---
author: Centurio
categories:
- NAS
date: "2012-12-22T23:19:37Z"
guid: http://centurio.net/?p=2014
id: 2014
image: /wp-content/uploads/2012/12/IMG_1291.jpg
tags:
- mdraid
- Raid
- Synology
title: 'Synology DS213+: Raid 1 oder SHR'
url: /2012/12/22/synology-ds213-raid-1-oder-shr/
---
Wenn man die Synology DS213+ zum ersten mal einrichtet, dann fragt einen der Assistent wie man mit den verbauten Festplatten umgehen möchte. Zur Auswahl stehen dann unter anderem die Konfiguration ohne ein RAID (also bei mir 2\*3TB = 6TB Speicher) oder die Konfiguration eines RAID (0 oder 1, 2\*3TB = 6TB am Stück, oder 2*3TB = 3 TB mit Auswahlsicherheit).

Ich habe mich für die RAID 1 Variante entschieden. Wenn man die Konfiguration abgeschlossen hat, formatiert die Maschine im Hintergrund das Dateisystem entsprechend und legt den RAID Verband an. Was mir dabei aufgefallen ist: Es gibt ein RAID 1 wie man es kennt und es gibt ein SHR RAID 1. Bei SHR handelt es sich um das [Synology Hybrid Raid](http://www.synology.com/support/tutorials_show.php?q_id=492). Dieses ist empfohlen für normale Benutzer, die Wert auf größtmögliche Flexibilität &nbsp;und Einfachheit legen. Also eigentlich ist die Wahl nicht schlecht. Schließlich ermöglicht sie es unproblematisch unterschiedlich große Festplatten optimal zu nutzen. Allerdings habe ich mit meinen 2\*3TB schon fast die höchste Ausbaustufe von 2\*4TB erreicht. Dabei dachte ich mir dann, das ich vermutlich eh nicht mehr die Festplatten bei dem Gerät tauschen werde und eher ein neues NAS aufbauen würde.

Also war der Wunsch nach dem klassischen RAID 1 da. Dabei sollte es sich dann um ein über das Linux Tool eingerichtetes md device handeln, das man mit [mdadm](http://wiki.ubuntuusers.de/Software-RAID) entsprechend kontrollieren kann. Doch um diese Information erst mal zu finden musste ich über eine Stunde im [synology-forum.de](http://www.synology-forum.de) suchen und mir verschiedene Meinungen durchlesen. Dort wird meistens das SHR RAID empfohlen, während in einer Abstimmung ein Großteil der Nutzer das klassische RAID 1 benutzen. Dies muss also einen Sinn haben, dachte ich mir. Auf zur Grundlagenforschung:

Nun, die älteren Versionen der DiskStation Software (so nennt sich das Betriebssystem der Geräte von Synology) konnten wohl nur das klassische RAID verwenden. Und da ein Großteil der Nutzer Synology Geräte entsprechend lang benutzt denke ich mir mal, das die meisten ihre Festplatten einfach migriert haben und daher RAID 1 nutzen.

Für SHR spricht halt die große Flexibilität, die sich allerdings erst bei Geräten mit mehr als 2 Schächten bemerkbar macht.

Mich plagte aber noch eine andere Frage: Was passiert, wenn die DS mal abraucht und ich nicht mehr an meine Daten komme? Die Festplatten sind mit ext4 formatiert&#8230; Aber wie bekomme ich das RAID gemountet am PC? Der entsprechende Wiki Eintrag behandelt nur Software, die Zugriff auf ext4 unter Windows ermöglicht oder von älteren Versionen spricht.. Zugriffe auf das RAID selber werden nicht erklärt. Und allein bin ich mit der Frage auch nicht.

Also suchte ich weiter und fand in [diesem Thread](http://www.synology-forum.de/showthread.html?32821-Festplatte-unter-Linux-mounten) immerhin ein paar Antworten. Demnach ist das SHR wohl der von Linux benutzte [LVM (Logical Volume Manager)](http://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)). Würde ich also mal versuchen die Festplatte am PC so zu mounten, so hätte ich zusätzlich zum RAID Problem noch das LVM Problem am Hals.

Daher habe ich mich entschlossen, lieber das &#8222;native&#8220; RAID 1 zu verwenden. Hier sollte man dann im Notfall von einer Linux Live CD booten können und hätte dann die Möglichkeit das md Device zu erstellen, auch wenn nur noch eine Platte vorhanden ist. Von diesem Device könnte man dann die ext4 Partition mounten. Idealerweise wäre das dann:

<pre>sudo mdadm --assemble --scan</pre>

Danach könnte man dann mit der Beschreibung aus dem Wiki zu Datenrettungstools fortfahren, bzw. man liest weiter im [Ubuntu Wiki](http://wiki.ubuntuusers.de/Software-RAID).