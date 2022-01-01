---
author: Centurio
categories:
- Apple
date: "2009-10-07T16:35:56Z"
guid: http://centurio.net/?p=1193
id: 1193
title: 10.6.1 und Probleme mit komplexen Samba Passwörtern
url: /2009/10/07/10-6-1-und-probleme-mit-komplexen-samba-passwortern/
---
Irgendwas war dann doch anders, nachdem ich auf 10.6 das Upgrade gemacht habe&#8230; Ich konnte nicht mehr auf die Samba Freigabe meiner Fritzbox zugreifen.

Doch was kann das Problem sein?  
<!--more-->

Nachdem ich mich per SSH auf der Fritzbox eingelogt habe, konnte ich merkwürdige Fehlermeldungen über eine falsche Codepage finden. Da dachte ich schon &#8222;Oh man, das neue Trunk Image (Entwicklerversion aus dem SVN) der Fritzbox funktioniert mal wieder nicht&#8220; und da habe ich schon wieder angefangen neue Firmware zu kompilieren. Allerdings wars das dann doch nicht.

Das Passwort des Samba Accounts habe ich dann auch ein paar mal geändert bzw. neu eingetragen, aber es hat einfach nichts gebracht. Der Finder von Mac OS hat einfach die Verbindung verweigert und wollte mir irgendwas davon erzählen, dass die Freigabe nicht verfügbar wäre.

Nachdem ich dann aber etwas [gegoogelt](http://www.google.de/search?q=10.6+smb+probleme) habe, bin ich schließlich im Apple Support Forum fündig geworden: Man muss das Passwort auf alphanumerisch umstellen, sprich nur Zahlen im Passwort verwenden. 

Das das ganze natürlich unpraktikabel ist und auch nicht sonderlich sicher ist, sollte klar sein. Jedoch ist es im Moment die einfachste Möglichkeit wieder an die Daten der FritzBox zu kommen. Schade. Ich hoffe, dass Apple in 10.6.2 das entsprechend fixt&#8230;