---
author: Centurio
categories:
- Internet und co
- Security
date: "2009-05-22T13:30:02Z"
guid: http://centurio.net/?p=1132
id: 1132
tags:
- Chrome
- EVC
- google
- HTTPS
- SSL
- Uni
title: Google Chrome und die Extended Validation Certificates
url: /2009/05/22/google-chrome-und-die-extended-validation-certificates/
---
Also irgendwas mache ich falsch, oder ich verstehs einfach nur nicht, vielleicht weiß ja einer von euch woran das liegt:

Wieso zeigt der Google Chrome Browser z.B. bei der Online-Banking Seite der Dresdner Bank nicht die Bank in der Adressleiste an? Moderne Webseiten wollen dem Nutzer einfach und schnell einen Überblick geben, ob sie auch wirklich die Seiten sind, die sie sein sollten. Dazu gibt es für SSL Zertifikate eine Erweiterung, die sich Extended Validation nennt. Dabei werden die Webseitenbetreiber/Antragssteller einer genaueren Prüfung als sonst üblich unterstellt und erhalten dann für ihr Zertifikat diese Erweiterung.

Besucht man dann eine Webseite mit dieser Erweiterung, zeigt der Browser einem ein oder mehrere Extrafelder an, dass es sich auch wirklich um den Betreiber dieser Seite handeln soll.

Beim IE 8 sieht das z.B. so aus:<figure id="attachment_1133" aria-describedby="caption-attachment-1133" style="width: 150px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2009/05/ie\_dresdnerbank.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title="">

<img loading="lazy" src="http://centurio.net/wp-content/uploads/2009/05/ie_dresdnerbank-150x150.jpg" alt="Internet Explorer 8, EVC Meldung dresdner-privat.de" title="Internet Explorer 8, EVC Meldung dresdner-privat.de" width="150" height="150" class="size-thumbnail wp-image-1133" /> </a><figcaption id="caption-attachment-1133" class="wp-caption-text">Internet Explorer 8, EVC Meldung dresdner-privat.de</figcaption></figure> 

Beim Firefox 3.0.10 sieht das so aus:<figure id="attachment_1134" aria-describedby="caption-attachment-1134" style="width: 150px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2009/05/ff\_dresdnerbank.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl_caption="" title="">

<img loading="lazy" src="http://centurio.net/wp-content/uploads/2009/05/ff_dresdnerbank-150x150.jpg" alt="Firefox 3.0.10, EVC Meldung dresdner-privat.de" title="Firefox 3.0.10, EVC Meldung dresdner-privat.de" width="150" height="150" class="size-thumbnail wp-image-1134" /> </a><figcaption id="caption-attachment-1134" class="wp-caption-text">Firefox 3.0.10, EVC Meldung dresdner-privat.de</figcaption></figure> 

Auf dem Mac sieht das mit dem Safari 4 Beta so aus:<figure id="attachment_1135" aria-describedby="caption-attachment-1135" style="width: 150px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2009/05/safari\_dresdnerbank.jpg" data-rel="lightbox-image-2" data-rl\_title="" data-rl_caption="" title="">

<img loading="lazy" src="http://centurio.net/wp-content/uploads/2009/05/safari_dresdnerbank-150x53.jpg" alt="Safari 4 Beta unter Mac OS X, EVC Meldung dresdner-privat.de" title="Safari 4 Beta unter Mac OS X, EVC Meldung dresdner-privat.de" width="150" height="53" class="size-thumbnail wp-image-1135" /> </a><figcaption id="caption-attachment-1135" class="wp-caption-text">Safari 4 Beta unter Mac OS X, EVC Meldung dresdner-privat.de</figcaption></figure> 

Wenn man sich jedoch jetzt den aktuellen Google Chrome unter Windows dann mal anschaut, sehe ich **keinerlei!** Meldung, die so ähnlich aussehen könnte:<figure id="attachment_1136" aria-describedby="caption-attachment-1136" style="width: 150px" class="wp-caption aligncenter"><a href="http://centurio.net/wp-content/uploads/2009/05/chrome\_dresdnerbank.jpg" data-rel="lightbox-image-3" data-rl\_title="" data-rl_caption="" title="">

<img loading="lazy" src="http://centurio.net/wp-content/uploads/2009/05/chrome_dresdnerbank-150x150.jpg" alt="Google Chrome, EVC Meldung dresdner-privat.de" title="Google Chrome, EVC Meldung dresdner-privat.de" width="150" height="150" class="size-thumbnail wp-image-1136" /> </a><figcaption id="caption-attachment-1136" class="wp-caption-text">Google Chrome, EVC Meldung dresdner-privat.de</figcaption></figure> 

Dass das ganze in Chrome gehen soll, zeigt z.B. die Schweizer Firma QuoVadis in ihrer [FAQ](http://www.quovadisglobal.ch/Support/FAQ.aspx).

Also ich verstehs echt nicht, wieso der Chrome das nicht anzeigt? Chrome und IE benutzen z.B. die gleiche Zertifikatsdatenbank, daher sind auch die Meldungen gleich beim Check des Zertifikats. Es handelt sich also nur um die fehlende Darstellung der EVC. Irgendwie erschrickt mich das ganze ja doch schon, ich dachte eigentlich, Google hätte das eingebaut...

Update: Hab den Fehler gefunden: Es liegt doch tatsächlich an der dämlich versteckten Option &#8222;Sperrung des Serverzertifikats überprüfen&#8220; in den Einstellungen Chromes. Aktiviert man dieses Kästchen, so wird der EVC Indikator dann auch mit angezeigt.