---
author: Centurio
categories:
- Apple
- Hardware
date: "2011-03-15T00:36:32Z"
guid: http://centurio.net/?p=1514
id: 1514
image: /wp-content/uploads/2011/03/SL_Install_fail.jpg
tags:
- EFI
- SATA
- SSD
title: MacbookPro5,5, OCZ Vertex SSD und Snow Leopard
url: /2011/03/15/macbookpro55-ocz-vertex-ssd-und-snow-leopard/
---
Ich habe gerade die Möglichkeit gehabt, eine OCZ Vertex SSD in meinem MacbookPro5,5 zu verbauen. Allerdings funktionierte die Installation von Snow Leopard überhaupt nicht (siehe Artikelbild) und mein erster Anhaltspunkt war eine zu alte Firmware Revision der SSD. Ich hatte jedoch bisher keine Möglichkeit ohne größere Umbauarbeiten die SSD an meinem Mac anzuschließen um die Firmware Revision auszulesen. Das werde ich bei Gelegenheit nachholen. **Update: Ich habe gerade mal an einem PC die SSD angeschlossen und es ist leider schon [die neueste Firmware 1.6](http://www.ocztechnology.com/ssd_tools/OCZ_Vertex_Limited_Edition_SSDs/) installiert. Schade.**  
<!--more-->

Eine weitere Fehlerquelle könnte wieder einmal der SATA Controller des Macbooks sein, schließlich hat dieser mit dem EFI Update 1.7 [einige](http://centurio.net/2010/02/15/festplattenaussetzer-auf-dem-macbookpro-133-verhindern/) [Probleme](http://centurio.net/2009/10/23/macbook-pro-13-zoll-snow-leopard-10-6-und-der-festplattenwechsel/) bereitet. In dem OCZ User Forum habe ich hingegen einen sehr interessanten Thread gefunden, der sich genau mit meinem Problem und diesem SSD Modell beschäftigt. Dort wird u.a. das Logicboard (bei Macs wird so das Motherboard genannt) als Fehlerquelle aufgeführt. Es gibt vom Logicboard zwei verschiedene Revisionen A und B. <a href="http://centurio.net/wp-content/uploads/2011/03/LogicboardMBP55.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/03/LogicboardMBP55-e1300142119542-300x158.jpg" alt="Logicboard Revision meines MacBookPro5,5" title="Logicboard Revision meines MacBookPro5,5" width="300" height="158" class="alignleft size-medium wp-image-1515" srcset="https://centurio.net/wp-content/uploads/2011/03/LogicboardMBP55-e1300142119542-300x158.jpg 300w, https://centurio.net/wp-content/uploads/2011/03/LogicboardMBP55-e1300142119542.jpg 609w" sizes="(max-width: 300px) 100vw, 300px" /></a>  
Mein Board wurde nie ausgetauscht und gehört daher der Revision A an, während der User im Forum wohl ein neues Logicboard mit Revision B verbaut bekommen hat und seitdem keinerlei Probleme mehr hat.

Ich frage mich jetzt natürlich, ob diese Logicboard Revision auch Probleme bei anderen SSDs mit neueren Controllern wie z.B. dem [Sandforce](http://en.wikipedia.org/wiki/SandForce) Chipsatz hat. Denn dann wäre der Kauf einer SSD vielleicht ähnlich riskant, insbesondere, wenn man beim Apple Care kein neues Logicboard bekommen könnte um das Problem zu umgehen. Leider habe ich aber auch keine Informationen zu diesem speziellen Problem gefunden, außer halt in dem o.g. Forum speziell zu dem SSD Typ.