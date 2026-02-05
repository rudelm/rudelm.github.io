---
author: Centurio
categories:
- NAS
- Photographie
date: "2012-12-31T15:45:19Z"
guid: http://centurio.net/?p=2030
id: 2030
image: /2012/12/22/synology-ds213-raid-1-oder-shr/images/DS213plus.jpg
tags:
- Aperture
- DS213+
- iPhoto
- Lightroom
- Synology
title: Synology DS213+ - PhotoStation mit iPhoto 11 und Lightroom 4

---
## Einleitung
Ich habe mir die DS213+ auch dafür gekauft um meine vielen Photographien sicher zu verstauen. Meistens brauche ich eh nicht mein komplettes Bilderarchiv und zweitens habe ich so mehr Platz unterwegs. Mein Ansatz war daher, dass ich den kompletten Bilder Ordner meines Macs auf das NAS in den photos Ordner kopiere. Dort würde er indiziert werden und würde dann der PhotoStation zur Verfügung stehen.

### Überlegungen
Von der Theorie her war der Ansatz nicht verkehrt, aber es gibt dabei einige Dinge zu beachten:

  * Es werden ALLE unterstützten Bilder indiziert und entsprechend wird auch dafür ein Thumbnail erstellt. Dies dauert sehr lange, wenn man denn nicht den Synology DiskStation Admin verwendet. 
  * Wenn man sehr viele Fotos hat, verliert man sehr schnell den Überblick.
  * Wenn man eine iPhoto oder Aperture Bibliothek auf das NAS kopiert, so werden sehr viele unnötige Thumbnails mit erstellt. iPhoto speichert in seinem Resourcen Bundle modifizierte Versionen als auch Originale ab, so hat man u.U. sehr viele unnötige Thumbnails doppelt.
  * iPhoto bzw. Aperture Bibliotheken funktionieren [nur auf HFS+ formatierten Volumes](https://discussions.apple.com/thread/2397680?start=0&tstart=0)!

Insbesondere der letzte Punkt stört mich. Jetzt könnte man natürlich ein DiskImage anlegen auf dem NAS, in dem wiederum die Bibliothek abgespeichert werden kann. Dann hat man allerdings wieder einen unnötigen Schritt dazwischen. Ich belasse daher meine iPhoto Bibliothek lieber auf meinem Mac und versuche dann mit TimeMachine von dieser Datenbank eine Kopie zu sichern.

Lightroom kann man so benutzen, das es Bilder nach Jahren und Tagen anlegt. Da würde eine Indizierung und Benutzung der PhotoStation prinzipiell möglich und einfacher sein, jedoch habe ich mich aufgrund [dieses Postings](http://www.synology-forum.de/showthread.html?34565-iPhoto-11.-Externer-Zugriff&p=284241&viewfull=1#post284241) dagegen entschieden. Stattdessen werde ich einfach nur die wirklich guten/wichtigen Photos in die PhotoStation einpflegen.