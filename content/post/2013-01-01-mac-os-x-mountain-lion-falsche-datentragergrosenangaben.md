---
author: Centurio
categories:
- Apple
date: "2013-01-01T22:18:00Z"
guid: http://centurio.net/?p=2035
id: 2035
image: /wp-content/uploads/2013/01/TimeMachine.png
tags:
- Finder
- Mac OS X
- Mountain Lion
- TimeMachine
title: Mac OS X Mountain Lion - Falsche Datenträgergrößenangaben
url: /2013/01/01/mac-os-x-mountain-lion-falsche-datentragergrosenangaben/
---
Ich habe mich gerade gewundert, wieso mein Mountain Lion mich mit falschen Datenträgergrößenangaben nervt und verwirrt. Ich habe eine 400GB große Partition, die aber eigentlich nur gut 200GB Daten beinhaltet.

<!--more-->

<a href="http://centurio.net/2013/01/01/mac-os-x-mountain-lion-falsche-datentragergrosenangaben/findergroesserichtig/" rel="attachment wp-att-2037"><img loading="lazy" class="aligncenter size-medium wp-image-2037" alt="Finder zeigt die richtige Größe an" src="http://centurio.net/wp-content/uploads/2013/01/FinderGroesseRichtig-300x278.png" width="300" height="278" srcset="https://centurio.net/wp-content/uploads/2013/01/FinderGroesseRichtig-300x278.png 300w, https://centurio.net/wp-content/uploads/2013/01/FinderGroesseRichtig.png 414w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Trotzdem meint das Festplattendienstprogramm, dass etwa 360GB belegt sind.

<a href="http://centurio.net/2013/01/01/mac-os-x-mountain-lion-falsche-datentragergrosenangaben/diskutilfalschegroesse/" rel="attachment wp-att-2036"><img loading="lazy" class="aligncenter size-medium wp-image-2036" alt="Festplattenverwaltung zeigt die falsche Größen an" src="http://centurio.net/wp-content/uploads/2013/01/DiskUtilFalscheGroesse-300x40.png" width="300" height="40" srcset="https://centurio.net/wp-content/uploads/2013/01/DiskUtilFalscheGroesse-300x40.png 300w, https://centurio.net/wp-content/uploads/2013/01/DiskUtilFalscheGroesse.png 610w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Woher kommt also diese Differenz von etwa 160GB? Ich habe ja [meine iTunes Bibliothek](http://centurio.net/2012/12/31/synology-ds213-itunes-bibliothek-verschieben/) verschoben sowie [meine Bilder](http://centurio.net/2012/12/31/synology-ds213-photostation-mit-iphoto-11-und-lightroom-4/). Dadurch habe ich also sehr viel auf der Festplatte geändert. Meine TimeMachine Festplatte habe ich während dieser Änderungen nicht mehr angeschlossen. Trotzdem hat das System im Hintergrund einfach versteckte lokale TimeMachine Einträge erzeugt. Diese Einträge belegen nun sehr viel Platz auf der Festplatte und werden nicht vom Finder oder von anderen Programmen entdeckt!

Bis ich zu dieser Erkenntnis kam dauerte es schon ziemlich lange. Mit dem Befehl

<pre>sudo tmutil disablelocal</pre>

kann man das lokale Backup deaktivieren. Nach einem Neustart wird der belegte Platz wieder freigegeben. Ich habe jetzt wieder meine 200GB frei. Jetzt sollte man aber das lokale Backup wieder einschalten mit dem Befehl

<pre>sudo tmutil enablelocal</pre>