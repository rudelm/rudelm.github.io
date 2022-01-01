---
author: Centurio
categories:
- Apple
date: "2011-08-03T17:25:11Z"
guid: http://centurio.net/?p=1644
id: 1644
image: /wp-content/uploads/2011/08/MoskauZeitzone.png
tags:
- Geo Location
- Lion
- Mac OS X
title: Mac OS X Lion und die Zeitzonen bzw. Geolocation
url: /2011/08/03/mac-os-x-lion-und-die-zeitzonen-bzw-geolocation/
---
Heute morgen schrieb ich in der Uni an meiner Masterarbeit. Dabei fiel mir dann irgendwann auf, dass es ja schon fast 11:50 wäre und eine Mittagspause angesagt wäre. Aber halt! Das kann doch gar nicht sein? Sollte die Zeit so schnell verflogen sein?

Ein Blick auf die Uhrzeit im Telefon als auch in meiner Windows VM verriet: Die Uhrzeit in Mac OS X Lion ist um 2 ganze Stunden nach vorne verschoben. Es war also eigentlich erst 9:50. U(h)rsache war in diesem Fall eine falsch erkannte Zeitzoneneinstellung in Mac OS:

<a href="http://centurio.net/wp-content/uploads/2011/08/MoskauZeitzone.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/08/MoskauZeitzone-300x207.png" alt="" title="Moskau Zeitzone" width="300" height="207" class="aligncenter size-medium wp-image-1645" srcset="https://centurio.net/wp-content/uploads/2011/08/MoskauZeitzone-300x207.png 300w, https://centurio.net/wp-content/uploads/2011/08/MoskauZeitzone.png 640w" sizes="(max-width: 300px) 100vw, 300px" /></a>

<!--more-->

Na super, was mache ich in denn in Moskau? Ich habe dann in allen Browsern versucht, eine HTML5 Geolocation Demo aufzurufen. Und auch hier wurde ich immer wieder in Moskau eingeordnet:

<a href="http://centurio.net/wp-content/uploads/2011/08/RusslandGeo.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/08/RusslandGeo-300x198.png" alt="" title="Russland Geolocation" width="300" height="198" class="aligncenter size-medium wp-image-1646" srcset="https://centurio.net/wp-content/uploads/2011/08/RusslandGeo-300x198.png 300w, https://centurio.net/wp-content/uploads/2011/08/RusslandGeo.png 764w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Nachdem ich schon das schlimmste vermutet habe und leicht nervös wurde, ob ich mir nicht doch mal ein wenig Malware eingefangen habe, war ich noch viel mehr genervt als meine Uhr immer wieder falsch lief und zwei Stunden Vorlauf hatte. Ich habe daher die automatische Lokalisierung deaktiviert und habe weiter experimentiert. Man kann in Mac OS X auch die Ortungsdienste in den Systemeinstellungen deaktivieren. Dann wird natürlich nicht mehr die Zeitzone korrekt automatisch erkannt. Gut, Hauptsache erst einmal weiter arbeiten können. Ich habe dann also die Zeit automatisch eingestellt, da der Zeitserver mir auch dauernd Moskau Zeit vorgeschlagen hat.

Die Lösung steckt scheinbar in den [Core Location Services](http://cocoawithlove.com/2009/09/whereismymac-snow-leopard-corelocation.html) von Mac OS. Diese funktionieren, wie auf dem iOS auch, nur mit Wlan/Funkmasten/GPS. Das evtl. die deutsche IP der Uni nicht dafür herangezogen wird, ist schon etwas merkwürdig gedacht. Als ich gerade wieder zuhause war, habe ich die Einstellungen erneut überprüft, dieses mal wird wieder korrekt Bochum angezeigt.

<a href="http://centurio.net/wp-content/uploads/2011/08/BochumZeitzone.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/08/BochumZeitzone-300x214.png" alt="" title="Bochum Zeitzone" width="300" height="214" class="aligncenter size-medium wp-image-1647" srcset="https://centurio.net/wp-content/uploads/2011/08/BochumZeitzone-300x214.png 300w, https://centurio.net/wp-content/uploads/2011/08/BochumZeitzone.png 640w" sizes="(max-width: 300px) 100vw, 300px" /></a>

Das war auf jeden Fall ein schneller Flug und ich bin froh, wieder in Bochum zu sein 😉 Scheinbar muss ein neuer Wlan Router in der Uni irgendwie die MAC oder die SSID eines Geräts in Moskau haben. Irgendwie schon doof, wenn einem dass dann spontan die Systemuhrzeit verstellt.