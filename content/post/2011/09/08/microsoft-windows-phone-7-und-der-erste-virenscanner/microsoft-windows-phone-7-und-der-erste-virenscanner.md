---
author: Centurio
categories:
- Security
- Windows Phone
date: "2011-09-08T07:19:41Z"
guid: http://centurio.net/?p=1650
id: 1650
tags:
- AV
- Microsoft
- WP7
title: Microsoft Windows Phone 7 und der erste Virenscanner
url: /2011/09/08/microsoft-windows-phone-7-und-der-erste-virenscanner/
---
**Small update: please [use Google Translate for an english version](http://translate.google.com/translate?sl=auto&tl=en&js=n&prev=_t&hl=en&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fcenturio.net%2F2011%2F09%2F08%2Fmicrosoft-windows-phone-7-und-der-erste-virenscanner%2F). I still need time to think about a good multilanguage solution for this blog 🙂**

Es war nur eine Frage der Zeit, bis der erste Virenscanner für Microsoft Windows Phone 7 erscheint. Gestern war es dann &#8222;endlich" soweit: [AVG Mobilation Anti-Virus Free](http://www.avgmobilation.com/products)

Nun ist es aber so, dass die App ganz normal vom Microsoft Marketplace geladen werden kann. Was bedeutet das für die App?

<!--more-->

  * Die App hat die gleichen Rechte wie jede andere App im Marketplace auch. D.h. sie hat minimale Rechte. Einzige Ausnahmen für Anwendungen mit mehr Rechten im Marketplace: Adobe Reader, Youtube und die ganzen OEM Anwendungen der Hersteller. AVG zählt **NICHT** dazu.
  * Windows Phone 7 nutzt ein Konzept, das sich Isolated Storage nennt. Dadurch darf jede Anwendung nur in ihrem eigenen Verzeichnis arbeiten und ist somit isoliert von den restlichen Apps. Die Apps haben untereinander keinerlei Verbindung und dürfen nicht auf Speicherbereiche außerhalb des ihnen zugeteilten Bereichs zugreifen.
  * Jede Anwendung muss im voraus deklarieren, welche Fähigkeiten (Capabilities) sie benutzt. Das kann z.B. Netzwerk (ID\_CAP\_NETWORKING), Lokalisierung (ID\_CAP\_LOCATION) oder Kamera (ID\_CAP\_CAMERA) sein. Sollte diese Fähigkeit nicht mit angegeben sein, so wirft das Programm beim Zugriff auf eine der Fähigkeiten die UnauthorizedAccessException. Des weiteren wird man vor dem Kauf auf die benötigten Fähigkeiten hingewiesen und auch gefragt beim Installieren/Kaufen/Herunterladen.

Soviel in Kürze zu den Grundlagen, die man haben muss, um zu verstehen, warum der AVG AV in seiner aktuellen Version eine sinnlose Software ist.

Warum behaupte ich, dass der AVG AV sinnlos ist? Nun ja, da gibt es mehrere Punkte:

  * Da die App wie jede andere App auch nur die nötigsten Rechte bekommt, kann es andere Speicherorte nicht untersuchen, geschweige denn irgendetwas desinfizieren oder löschen! Einzige Orte an denen gesucht werden kann sind die Multimedia Daten. Also Bilder, Videos und Musik.
  * [Rafael Rivera](http://www.withinwindows.com/2011/09/07/the-only-time-youll-see-avg-security-suite-warn-you-about-malware-on-windows-phone-7/) hat sich die Anti-Virus Definitionen angeguckt. Sie bestehen tatsächlich nur aus einer XML Datei, in der quasi nur &#8222;eicar" definiert ist. Eicar ist ein Testvirus, der benutzt werden kann um die Funktion eines Virenscanners zu überprüfen. Diese Anwendung sucht nur nach diesem String im Dateinamen [(Dank an Justin Angel)](http://www.justinangel.net) und schlägt dann Alarm.
  * Die angepriesene Safe Search und Safe Surf Funktion macht nichts weiteres, als den Suchbegriff im Eingabefenster an einen WebBrowserTask zu übergeben, der dann den Mobile Internet Explorer startet. Man wird dann auf eine Webseite von AVG weitergeleitet, die letztlich nur eine Google Suche ist. Für die Google Suche wird dann vermutlich die Google Safe Browsing API verwendet und das ist dann der einzige &#8222;Schutz".

Aber heute morgen hab ich dann noch eine schöne Neuigkeit über dieses Programm erfahren: Es benötigt die GPS Position des Telefons. Justin Angel hat dies herausgefunden und weiter analysiert:

  * Allgemeine Anleitung zum Nachfolgen seiner Schritte
  * Link zum aktuellen XAP Paket (Programmpaket)
  * Die betroffene Code Stelle und die Auflistung der gesammelten Informationen

Demnach erfasst die Anwendung die Position des Benutzers und so gut wie alle öffentlich auslesbaren Informationen auf dem Telefon. Dies sind dann z.B. Hardware Hersteller und Model, oder aber auch die eingerichtete E-Mailadresse. Die gesammelten Informationen werden dann an AVG geschickt.

Die Frage ist nun, was macht AVG damit? Ich habe da mehrere Theorien:

  * Wenn man AVG danach fragt, so werden sie bestimmt antworten: Wir benötigen diese Informationen zur Qualitätssicherung. Also auf welchen Geräten wird die Anwendung benutzt, wie oft, etc. Das müsste dann aber irgendwo in deren AGBs/Terms of Service stehen.
  * Die Daten sind eins zu eins übernommen aus der Android Anwendung. Die Anwendung auf Android kann wesentlich mehr, was aber auch am Design von Android liegt. Dort kann man das Handy lokalisieren lassen, es aus der Ferne löschen und sperren oder halt auch nach den zahlreich vorhandenen Android Viren suchen lassen.
  * Die Geo Daten werden für Ortsbasierte Suche verwendet.
  * Die gesammelten Daten werden für Marketingzwecke missbraucht.

Egal wie man es dreht, die Anwendung ist also wirklich nur sinnlos und bringt überhaupt keinen Zuwachs an Sicherheit. Stattdessen werden ahnungslose Nutzer dazu genötigt, über diese App zu suchen um sich sicher zu fühlen. In seiner aktuellen Form ist Windows Phone 7 recht sicher und Google kann man trotzdem selber vom Browser aufrufen.