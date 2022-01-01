---
author: Centurio
categories:
- Hardware
date: "2014-10-20T22:03:23Z"
guid: http://centurio.net/?p=2160
id: 2160
image: /wp-content/uploads/2014/10/FritzBox7490.jpg
tags:
- AVM
- DSL
- Fritz!Box
- Internet
- Powerline
- Repeater
- T Online
- VDSL
- Wlan
title: AVM Fritz!Box 7490 und AVM Fritz!WLAN Repeater 1750e
url: /2014/10/20/avm-fritzbox-7490-und-avm-fritzwlan-repeater-1750e/
---
Vor gut zwei Monaten habe ich einen VDSL 50 Anschluss der Telekom beauftragt. Als Router habe ich dazu die [AVM Fritz!Box 7490](http://www.amazon.de/gp/product/B00EO777DI) gewählt. Sie ist momentan das Top Model und bietet 802.11ac WLAN an. Das superschnelle WLAN, als auch das angeblich bessere (im Vergleich zur 7390) DSL Modem, haben mich dann zum Kauf bewegt. Schließlich habe ich mit meinem neuen MacbookPro auch endlich ein Gerät, das diese Geschwindigkeit ausnutzen kann.

Hier mal ein paar Punkte, die mir aufgefallen sind und mir auch gut gefallen:

  * 802.11ac WLAN funktioniert tatsächlich wahnsinnig gut. Ich habe etwa 2 Wände zwischen meinem Schreibtisch und dem Router, trotzdem kann ich immer noch mit gut 800MBit funken.
  * Das DSL Modem funktioniert hervorragend und hat die Leitung maximal ausgereizt (50MBit down, 10MBit up).
  * Das neue Fritz!OS 6.20 hat Unterstützung für meine [TP-Link TL-PA551](http://www.amazon.de/gp/product/B0041JKGW8) Powerline Adapter. Damit kann ich mir die eigentliche TP-Link Software sehr gut sparen.
  * Das WLAN Setup ist denkbar einfach. Spätestens, seitdem man auch QR Codes mit den Zugangsdaten direkt generiert bekommt.

Besonders begeistert war ich allerdings, als ich den [AVM Fritz!WLAN Repeater 1750E](http://www.amazon.de/gp/product/B00N80IK88) als Bridge eingerichtet hatte. So wird das Büro mit WLAN sowohl über 2,4GHz als auch über 5GHz mit dem Router verbunden. Es wird immer automatisch die schnellste bzw. stabilste Verbindung verwendet. Gegenüber dem Powerline Adaptern war das sicher eine sinnvolle Entscheidung. Scheinbar gibt es zuviele Störungen im Stromnetz, so dass ich hier Powerline nicht sehr schnell benutzen kann. Damit konnte ich auch nicht die volle VDSL 50 Geschwindigkeit ausnutzen. Mit dem Repeater lief es allerdings wieder auf voller Geschwindigkeit.

<a href="http://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" class="aligncenter size-medium wp-image-2162" src="http://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline-225x300.jpg" alt="Fritz!WLAN Repeater 1750E  & TP-Link551 Powerline Adapter" width="225" height="300" srcset="https://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline-225x300.jpg 225w, https://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline-768x1024.jpg 768w, https://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline-800x1066.jpg 800w, https://centurio.net/wp-content/uploads/2014/10/RepeaterPowerline-26x35.jpg 26w" sizes="(max-width: 225px) 100vw, 225px" /></a>

Wenngleich der Repeater im Moment auch schwer zu bekommen ist, so kann ich ihn durchaus immer wieder empfehlen! Die Einrichtung war spielend einfach (dank WPS Knopf) und die Performance ist einfach nur traumhaft.

Einziger Knackpunkt, den AVM aber auch in einer der nächsten Firmwareversionen hoffentlich fixen wird: Es ist keine feste IP Vergabe möglich für den Stick. Man kann ihn lediglich per DHCP auf eine IP setzen:

{{< tweet user="AVM_DE" id="520849380094386176" >}}

Die Kombination aus der Fritz!Box und dem Fritz!WLAN Repeater ist wirklich gut. Ich hätte theoretisch ja auch einen aktuellen AirportExpress wählen können, dann hätte ich allerdings vielleicht doch wieder Probleme mit irgendwelchen Besonderheiten oder Verschlüsselungen gehabt. Es gibt also nicht wirklich viel an der Box zu kritisieren. Sie erfüllt ihren Zweck, ist schnell und für mich absolut ausreichend (auch in Hinblick auf kommende DSL Generationen). Da ich sie auch als Telefonanlage mit DECT Telefon verwende, wäre eine verbesserte FAX Funktion noch nett. Der in der Weboberfläche eingebaute FAX Client kann nur Bilder verschicken, keine PDFs.