---
author: Centurio
categories:
- Hardware
- Linux
- Raspberry Pi
date: "2013-05-19T21:55:19Z"
guid: http://centurio.net/?p=2050
id: 2050
image: /wp-content/uploads/2013/05/raspbmc-time-settings.jpg
tags:
- Rasbmc
- XBMC
title: Rasbmc - falsche Zeitzoneneinstellung
url: /2013/05/19/rasbmc-falsche-zeitzoneneinstellung/
---
Seit einiger Zeit besitze ich ein [Raspberry Pi](http://www.raspberrypi.org/). Dieser kleine Computer ist sehr günstig (etwa 30 Euro) und kann als XBMC eingerichtet werden. Dabei habe ich mich für die [Rasbmc](http://www.raspbmc.com/) Distribution entschieden, da diese sehr einfach (ein Befehl auf der Konsole) installiert werden kann.

&nbsp;

Bereits bei der Ersteinrichtung wird man nach der aktuellen Zeitzone gefragt. Hier habe ich natürlich für Deutschland Berlin als Stadt und Europa als Region ausgewählt. Leider zeigt mir mein XBMC aber die Uhrzeit immer um zwei Stunden nach hinten versetzt an. Wenn also jetzt 21:47 ist, dann zeigte XBMC 19:47 an.

&nbsp;

Eine kurze Google Recherche [ergab dann](http://strobelstefan.org/?p=2682), dass man den Assistenten zur Einrichtung der Zeitzone erneut aufrufen kann. Dazu tippt man

`sudo dpkg-reconfigure tzdata`

ein. Der Assistent führt einen dann durch die Konfiguration und sieht dann in etwa so aus:

<a href="http://centurio.net/wp-content/uploads/2013/05/raspbmc-geographic-area.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2051" alt="Rasbmc - Geographic Area" src="http://centurio.net/wp-content/uploads/2013/05/raspbmc-geographic-area-300x238.png" width="300" height="238" srcset="https://centurio.net/wp-content/uploads/2013/05/raspbmc-geographic-area-300x238.png 300w, https://centurio.net/wp-content/uploads/2013/05/raspbmc-geographic-area.png 571w" sizes="(max-width: 300px) 100vw, 300px" /></a> <a href="http://centurio.net/wp-content/uploads/2013/05/raspbmc-region.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2052" alt="Raspbmc - Region" src="http://centurio.net/wp-content/uploads/2013/05/raspbmc-region-300x239.png" width="300" height="239" srcset="https://centurio.net/wp-content/uploads/2013/05/raspbmc-region-300x239.png 300w, https://centurio.net/wp-content/uploads/2013/05/raspbmc-region.png 572w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Doch das reichte noch nicht aus, um auch wirklich die richtige Uhrzeit anzuzeigen. Man muss in den [Darstellungsoptionen des XBMC](http://www.forum-raspberrypi.de/Thread-raspbmc-zeigt-nur-utc-zeit) ebenfalls die Region und den Ort auswählen. Ich hatte eigentlich erwartet, das diese Einstellung übernommen wird, aber dem ist leider nicht so. Die richtigen Einstellungen für Deutschland sieht man auf dem Screenshot:

<a href="http://centurio.net/wp-content/uploads/2013/05/raspbmc-time-settings.jpg" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2053" alt="Raspbmc - Time Settings" src="http://centurio.net/wp-content/uploads/2013/05/raspbmc-time-settings-300x225.jpg" width="300" height="225" srcset="https://centurio.net/wp-content/uploads/2013/05/raspbmc-time-settings-300x225.jpg 300w, https://centurio.net/wp-content/uploads/2013/05/raspbmc-time-settings-1024x768.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" /></a>

&nbsp;