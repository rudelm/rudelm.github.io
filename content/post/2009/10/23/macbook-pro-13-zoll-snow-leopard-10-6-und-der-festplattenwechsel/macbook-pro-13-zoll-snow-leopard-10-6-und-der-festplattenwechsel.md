---
aktt_notify_twitter:
- "no"
author: Centurio
categories:
- Apple
- Hardware
date: "2009-10-23T12:29:03Z"
guid: http://centurio.net/?p=1222
id: 1222
tags:
- Mac OS X
- Snow Leopard
title: Macbook Pro 13 Zoll, Snow Leopard 10.6.1 und der Festplattenwechsel
url: /2009/10/23/macbook-pro-13-zoll-snow-leopard-10-6-und-der-festplattenwechsel/
---
160GB waren mir eindeutig zu wenig in meinem Macbook. Also habe ich direkt eine 500GB Festplatte von Western Digital geordert, nämlich die WD Scorpio Blue WDC WD5000BEVT. Also eine sehr gute und günstige Festplatte (siehe [Test der PC-Welt](http://www.pcwelt.de/start/computer/festplatte_storage/tests/194267/wd5000bevt/)).  
<!--more-->

Während unter Mac OS 10.5.8 keine Probleme bemerkbar waren, hatte ich unter 10.6 häufiger Probleme. Diese äußerten sich in einer sehr merkwürdigen Art von Hängern.

Man hört Musik in iTunes und surft eine Runde. Dabei lädt man im Hintergrund eine Datei herunter. Jetzt will man irgendeinen Link anklicken oder ein Finder Fenster öffnen und da passiert es: Man bekommt den Beachball/Spinning Wheel of death zu sehen. Quasi das Pendant zur Sanduhr der Windows Welt.

Gut, das an sich ist ja nicht schlimm, manchmal braucht der Mac halt seine Zeit um was zu öffnen. Jedoch wundert es mich, dass dieser Beachball unterschiedlich lang (manchmal 30s) zu sehen ist und dann nichts mehr reagiert. Wenn sich das System gefangen hat, sind alle Programme wieder verfügbar. Downloads sind weiter fortgeschritten und sind nicht abgebrochen. Es scheint also echt so zu sein, dass das System auf die Festplatte wartet und im Hintergrund im Speicher weiterarbeitet.

Nun wurde vor einiger Zeit auch für 10.6 ein Software Update ([Performance Update 1.0](http://www.golem.de/0910/70514.html)) vorgestellt, das genau diese Performance Probleme beseitigen sollte. Dieses Update habe ich natürlich installiert, aber habe davon nichts festgestellt.

Zweite Möglichkeit: Das verflixte [EFI Update 1.7](http://support.apple.com/kb/HT3561?viewlocale=de_DE), das leider auch nicht wieder entfernt werden kann. Es soll Probleme beheben im Zusammenspiel mit SATA und dem eingebauten SATA Controllerchip. Dieser scheint in dem Auslieferungszustand nur Festplatten im SATA1 Modus nutzen zu können. Dann ist die Geschwindigkeit auf 1,5GBit/s eingestellt, während moderne Festplatten alle den SATA2 Modus verwenden mit 3,0GBit/s.

Apple liefert seine Festplatten immer als SATA1 Version aus, mit denen das MBP dann auch keine Probleme hat und wunderbar funktioniert. Doch wehe, man hat eine eigene Platte eingebaut (um z.B. die horrenden Plattenpreise von Apple zu umgehen). Dann kann man [Probleme](http://www.mactechnews.de/news/index.html?id=144345) mit dem EFI Update bekommen. Bei [vielen Leuten](http://www.maclife.de/news/betriebssystem/andere/raetselhaftes-problem-mit-macbook-pro-efi-update-und-sata-festplatten) war es sogar so, dass die fremden Festplatten überhaupt nicht mehr funktionierten.

Der Rat lautet also im Moment: [Nicht Updaten!](http://www.golem.de/0907/68250.html)

Ich kenne in meinem Bekannten Kreis nur eine weitere Person, die die identische Hardwareausstattung wie ich auch habe, und diese Person hat auch ab und an diese Hänger, es handelt sich also vermutlich echt um ein Problem mit dieser Festplatte und dem verbauten SATA Controller Chip.

Gestern habe ich dann mal meinen Mac kurz demontiert um die Festplatte mit genauer anzusehen. Dort sind 4 Jumper zu sehen, die allerdings nichts mit dem einzustellenden SATA Mode zu tun haben. Früher konnte man in der Übergangsphase von SATA1 auf SATA2 die Festplatten dazu zwingen, im SATA1 Mode zu laufen. Dies ist heutzutage leider nicht mehr möglich. Selbst mit der Diagnose Software von WD kann man nicht den Acoustic Mode oder den SATA Mode mehr einstellen ([Windows](http://support.wdc.com/product/download.asp?groupid=702&sid=3&lang=de) und [Dos](http://support.wdc.com/product/download.asp?groupid=702&sid=30&lang=de) Version).

Tja, verdammt. Was macht man nun da? Einfach abwarten und mit dem Problem leben? Oder solange versuchen Apple vollzuheulen, bis die was ändern? Wird auf jedenfall alles irgendwie nervig und vermutlich sinnlos sein :/