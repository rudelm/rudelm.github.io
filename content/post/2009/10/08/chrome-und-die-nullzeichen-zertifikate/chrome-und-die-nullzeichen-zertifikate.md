---
aktt_notify_twitter:
- "no"
author: Centurio
categories:
- Internet und co
- Security
date: "2009-10-08T11:01:15Z"
guid: http://centurio.net/?p=1203
id: 1203
title: Chrome und die Nullzeichen Zertifikate
url: /2009/10/08/chrome-und-die-nullzeichen-zertifikate/
---
Da lese ich gerade bei [Heise](http://www.heise.de/security/meldung/Gefaelschtes-PayPal-Zertifikat-taeuscht-IE-Chrome-und-Safari-811918.html), das jetzt ein Zertifikat speziell für www.paypal.com angepasst wurde, um Probleme mit der Nullzeichenfilterung in SSL-Zertifikaten zu verdeutlichen. Damit sollen die Entwickler aufgerüttelt werden, endlich etwas gegen diesen Fehler zu unternehmen.

Nun gut, jetzt schreibt der Autor aber, dass in Chrome die zugehörige Überprüfung von Zertifikaten abgeschaltet sein sollte.

In meiner Bachelorarbeit habe ich mich ja auch gerade mit dem Thema beschäftigt und bei mir war diese Option in der aktuellen Chrome 3 Version (also keine Entwickler- oder sonstwie-beta-Version) auch aktiviert. <del datetime="2009-10-08T15:10:08+00:00">Das habe ich jetzt auf mehreren Rechnern schon testen können.</del> Ich habe jetzt noch mehr Rechner damit mal befüllt und siehe da, die Option scheint echt deaktiviert zu sein ?! fragt sich nur, warum das auf den Rechnern von mir an war oder ich mir da selber das Ergebnis mit einer uralten Installation verfälscht habe 🙁

Was stimmt denn nun? Könnt ihr das auch mal ausprobieren und bei euch nachgucken? Zu finden ist das unter dem Schraubenschlüsselsymbol rechts oben im Browser, dann unter Optionen und anschließend unter Sicherheit muss der Punkt &#8222;Sperrung des Zertifikats überprüfen&#8220; gesetzt sein. Die von mir getestete Version ist die aktuelle 3.0.195.25. Im [Heise Forum](http://www.heise.de/security/news/foren/S-Re-Sperrung-des-Serverzertifikats-war-bei-meinem-Chrome-schon-aktiviert/forum-167091/msg-17468711/read/) wundern sich über diese Tatsache auch schon einige Leute und für mich wäre das natürlich noch ein Punkt, den ich eventuell beachten müsste. 

Zwar schützt diese Option nicht vor erneuten Angriffen mit dem Nullzeichenfehler, aber zumindest verhindert sie bei bekannteren Zertifikaten größeres Unheil, in dem der Nutzer vorher bei Betreten der Seite gewarnt wird.