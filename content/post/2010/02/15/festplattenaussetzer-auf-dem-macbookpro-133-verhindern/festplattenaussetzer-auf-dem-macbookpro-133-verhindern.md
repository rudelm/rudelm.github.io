---
author: Centurio
categories:
- Apple
- Hardware
date: "2010-02-15T13:45:40Z"
guid: http://centurio.net/?p=1302
id: 1302
tags:
- Festplatten
- MacBookPro
- meinung
- Western Digital
title: Festplattenaussetzer auf dem MacbookPro 13,3" verhindern
url: /2010/02/15/festplattenaussetzer-auf-dem-macbookpro-133-verhindern/
---
Ich habe mich ja schon [vor einiger Zeit](http://centurio.net/2009/10/23/macbook-pro-13-zoll-snow-leopard-10-6-und-der-festplattenwechsel/) mal darüber aufgeregt, dass ich in meinem 13,3" MacbookPro extremste Probleme mit der Festplatte hatte. Das äußerte sich z.B. in einem System, das nicht mehr auf meine Anfragen reagiert, aber nach etwa 30 bis 60 Sekunden wieder normal weiter läuft und tut, als ob nichts passiert wäre.

Mittlerweile habe ich das bei mir an anderer Stelle nicht empfohlene EFI Update für 3GBit Sata installiert und hatte noch immer die Probleme.

<!--more-->

[Ein Support Dokument von Apple](http://support.apple.com/kb/HT1934?viewlocale=de_DE) bzw. ein kleiner Tipp eines Kommilitonen mit einem weißen Macbook und der gleichen Festplatte sorgte dann doch für schnelle Abhilfe:

Die Western Digital Scorpio Blue 500GB Festplatte verfügt über einen eingebauten Bewegungssensor, der den Festplattenkopf parkt wenn Erschütterungen zu stark werden. An sich ist das ein wirklich gutes Feature und es ist mit Sicherheit auch sinnvoll. Jedoch kommt eben genau dieses Feature in die Quere mit dem Bewegungssensor des MacbookPro. Dieser Sensor soll dort genau das gleiche Verhindern.

[<img loading="lazy" src="http://farm4.static.flickr.com/3342/3220142543_013b020247.jpg" width="500" height="375" alt="500GB WD Scorpio Blue" />](http://www.flickr.com/photos/rbitting/3220142543/ "500GB WD Scorpio Blue von Bitman bei Flickr")

Nun müsste man aber ja annehmen, dass wenn das Notebook ganz still auf dem Schreibtisch steht und man darauf rumtippt es eigentlich keine Probleme mit Bewegungen geben sollte. Dem ist nun leider nicht so, weswegen ich auch nie geglaubt hätte, dass die Lösung funktioniert:

Man kann mittels eines kleinen Befehls auf der Konsole den internen Bewegungssensor des MacbookPros deaktivieren. Dieses Vorgehen wird von Apple z.B. für DJs in Diskotheken empfohlen, die dort ihr Macbook den starken Erschütterungen eines Basslautsprechers z.B. aussetzen um dort Musik zu machen. 

Der Befehl lautet:  
`sudo pmset -a sms 0 ausschalten, mit sudo pmset -a sms 1 einschalten`

Nachdem ich diesen Befehl ausgeführt hatte, habe ich seit etwa einem Monat meine Ruhe. Das MacbookPro läuft wieder ordentlich, so wie ich es von dem Gerät erwartet hätte. Schade, dass solch Kleinigkeiten einen in den Wahnsinn treiben können.

Die Alternativen wären jetzt eigentlich ohne diesen Befehl nur noch ein Neukauf einer anderen Platte ohne dieses <del datetime="2010-02-15T11:25:00+00:00">Bug</del> "Feature&#8220; (z.B. als SSD) oder das Deaktivieren des Festplattenbewegungssensors. Laut Western Digital Support ist das aber bei dieser Festplatte nicht möglich...

**Update:** hier sind mal XBench Vergleichswerte von meiner WD Platte und der Hitachi Platte, die mein Vater verbaut hat. Mal ist meine schneller, dann wieder seine. Im alllgemeinen glaube ich aber, die Hitachi ist minimal langsamer in bestimmten Situationen:  
<a href="http://centurio.net/wp-content/uploads/2010/02/Xbench\_WD500BEVT.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2010/02/Xbench_WD500BEVT-300x295.jpg" alt="" title="Xbench Erbegnisse meiner WD Scorpio Blue 500GB Festplatte" width="300" height="295" class="aligncenter size-medium wp-image-1306" srcset="https://centurio.net/wp-content/uploads/2010/02/Xbench_WD500BEVT-300x295.jpg 300w, https://centurio.net/wp-content/uploads/2010/02/Xbench_WD500BEVT.jpg 601w" sizes="(max-width: 300px) 100vw, 300px" /></a>  
<a href="http://centurio.net/wp-content/uploads/2010/02/XBench\_Hitachi\_1.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_1-300x294.png" alt="" title="XBench Ergebnisse der Hitachi Festplatte meines Vaters: Test 1" width="300" height="294" class="aligncenter size-medium wp-image-1307" srcset="https://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_1-300x294.png 300w, https://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_1.png 524w" sizes="(max-width: 300px) 100vw, 300px" /></a>  
<a href="http://centurio.net/wp-content/uploads/2010/02/XBench\_Hitachi\_2.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_2-300x296.png" alt="" title="XBench Ergebnisse der Hitachi Festplatte meines Vaters: Test 2" width="300" height="296" class="aligncenter size-medium wp-image-1308" srcset="https://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_2-300x296.png 300w, https://centurio.net/wp-content/uploads/2010/02/XBench_Hitachi_2.png 604w" sizes="(max-width: 300px) 100vw, 300px" /></a>

**Update 2:**  
Hier sind noch ein paar Links zu Eerfahrungsberichten mit den 640, 750 und 1000GB Scorpio Blue Festplatten von WD auf dem Mac:

  * [First Report/Benchmarks of WD 1TB Scorpio HD in Unibody MacBook Pro](http://www.xlr8yourmac.com/feedback/1TB_WD_Scorpio_in_Macs.html)
  * [Western Digital 750GB (and 640GB) Scorpio HDs in Unibody MacBook/Pros](http://www.xlr8yourmac.com/feedback/WD750GB_Scorpio_in_Macs.html)
  * Does your Apple notebook hard drive (HDD) ever sound like little mice are playing table tennis inside of it? Or, why your HDD might be pre-programmed for quick failure.