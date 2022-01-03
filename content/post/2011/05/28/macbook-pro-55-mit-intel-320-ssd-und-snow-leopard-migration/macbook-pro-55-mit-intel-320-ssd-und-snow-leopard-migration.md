---
author: Centurio
categories:
- Apple
- Hardware
- Shopping
date: "2011-05-28T13:31:41Z"
guid: http://centurio.net/?p=1559
id: 1559
image: /wp-content/uploads/2011/05/ssd6.jpg
tags:
- Intel 320
- Optibay
- SSD
- Warenkorb
title: Macbook Pro 5,5 mit Intel 320 SSD und Snow Leopard Migration
url: /2011/05/28/macbook-pro-55-mit-intel-320-ssd-und-snow-leopard-migration/
---
Endlich ist es soweit: Nach vielen Monaten der Überlegungen und vielem ausprobieren habe ich mir eine Intel 320 SSD mit 120GB Speicherplatz gekauft. Die Entscheidung eine SSD zu kaufen wurde mir glücklicherweise ziemlich leicht gemacht. Ein guter Freund von mir hat mir seine neue Intel 320 mit 300GB testweise geliehen, so dass ich erst einmal Testen konnte, ob ich denn nicht [wieder den elendigen Beachball](http://centurio.net/2010/05/08/western-digital-vs-hitachi-festplatten-im-mbp55/) bekomme und dauernd auf die Festplatte warten muss oder [ob ich überhaupt installieren kann](http://centurio.net/2011/03/15/macbookpro55-ocz-vertex-ssd-und-snow-leopard/).

Nun, dieser Test funktionierte sogar so gut und meine Begeisterung darüber war so groß, dass ich mir direkt vor 3 Tagen die SSD und einen Optibay Adapter über Ebay besorgt habe. Ich wollte so schnell es geht die Hardware zusammen haben und mich an das umbauen setzen.

<!--more-->

Geplant war folgendes: Meine alte 500GB Hitachi HDD sollte in einen sogenannten Optibay Adapterrahmen und die Stelle einnehmen, wo vorher das Slotin Superdrive meines Macbook saß. Dazu kaufte ich mir nach langen Überlegungen bei Ebay den Adapter, und nicht bei [Hardwrk.com](http://hardwrk.com/macbook-ssd-hdd-adapter-kit.html) oder bei mac-optibay.de. Bei beiden waren mir die Lieferzeiten und Preise im allgemeinen zu hoch. Zwar ist das Set von Hardwrk.com schon ziemlich gut, aber die guten Wiha Schraubendreher, als auch den Plastikspatel hätte ich dann doppelt besessen. Also habe ich etwas recherchiert und alle Anbieter verbauen letztlich die gleichen Einbaurahmen der Firma Fenvi. Diesen Rahmen bekommt man manchmal auch schon für lediglich 5 Euro aus Hong Kong, nur muss man dann entsprechend lange darauf warten können. Also nichts für Ungeduldige wie mich 😉 Mein Ebay Anbieter hatte so einen Rahmen privat verkauft. Auf alle meine Fragen konnte er mir schnell eine Antwort geben und er garantie sogar, dass die Ware noch am gleichen Tag mit der Briefpost verschickt werden sollte. Da konnte ich natürlich nicht mehr wiederstehen. Genauso wenig wie bei der SSD, welche ich bei MIX Computer gekauft habe. Beide Anbieter kann ich definitiv empfehlen, da die Hardware bereits nach 24h bei mir zuhause ankam!

Nachdem ich ein Bootfähiges Backup mit [SuperDuper!](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html) auf einer meiner externen Festplatten angefertigt hatte, konnte ich mich endlich an die Installation der neuen Hardware wagen. Hier verweise ich auf die sehr gute Einbauanleitung von hardwrk.com, zu der ich eigentlich nicht mehr viel zusätzlich sagen kann, außer dass ich die beiden übergebliebenen Schrauben in das alte SuperDrive geschraubt habe, um sie nicht zu verlieren. Wo wir gerade beim SuperDrive sind: Ich habe keinen Bedarf für das externe Gehäuse gehabt, da ich bereits einen sehr guten externen USB 2.0 DVD Brenner von Samsung besitze und man für knapp 40 Euro auch einen extra dafür konstruierten externen USB 2.0 DVD Brenner kaufen kann. Dieser hat dann auch den Vorteil, dass er komplett Staubdicht ist und auch meistens wesentlich bessere Laufwerke verbaut sind, als in den Apple Rechnern immer steckt.

Nach erfolgreichem Umbau und Zusammenbau des Notebooks habe ich mich erneut an [die Migrationsanleitung von Hardwrk.com](http://hardwrk.com/anleitung/migrationsanleitung/) gehalten und möchte hier noch ein paar Kleinigkeiten ergänzen, die mich gestern bzw. heute morgen doch gestört haben. Die Anleitung schlägt vor, dass man OS X auf die SSD installiert, dort einen temporären Benutzer erstellt und nach erfolgreicher Installation den Migrationsassisten startet. Mit Hilfe des Assistenten kann man dann nur den Benutzer und seine Einstellungen übertragen lassen. Dazu kann man dann entweder sein letztes TimeMachine Backup wählen oder aber die intern verbaute HDD mit der alten Installation. Diese ist vorzuziehen, da man dann mit bis zu 70MB/s die Migration vornehmen kann. Solltet ihr also euer Backup auf einer Thunderbolt/eSata Festplatte liegen haben, solltet ihr die dann natürlich lieber nehmen 😉

Wenn dieser Benutzer nun migriert ist, muss man noch das Homeverzeichnis des migrierten Users auf die externe Festplatte umleiten. Dies kann man über die Systemeinstellungen, Benutzer machen indem man mit einem Rechtsklick auf den User die erweiterten Eigenschaften anzeigen lassen kann. Hierbei gibt es eine Sache, die mir aufgefallen ist: Wenn man unzufrieden ist mit der Bezeichnung seiner internen HDD (bei den meisten Leuten heißt die z.B. Macintosh HD) und möchte den Namen der HDD abändern, nachdem man hier das Homeverzeichnis geändert hat, so kann man sich nicht mehr vernünftig mit diesem User anmelden. Also wenn man eine Namensänderung vornehmen will, so sollte man dies vor der Umstellung des Homeverzeichnisses durchführen.

Hat man diese Hürde genommen, so kann man sich jetzt noch mit einem Symbolischen Link auf das neue Homeverzeichnis viel Arbeit ersparen. Beim Migrieren hat OS X alle Inhalte des alten User Verzeichnisses übertragen. Dazu gehören bei mir auch jede Menge versteckte Ordner, die je nach System auch schon mal einiges an Platz wegnehmen können. Nachdem ihr euch sicher seid, dass ihr euch im richtigen Verzeichnis (auf der SSD in /home) befindet und ihr dort keine wichtigen Dateien mehr habt, könnt ihr mit `rm -rf Username` das komplette migrierte Temporäre Benutzerverzeichnis löschen. Jetzt muss man nur noch einen Symbolischen Link auf den User Ordner auf der internen HDD mit dem Befehl `sudo ln -s /Volumes/HDD/Users/Username /Users/Username` erstellen. Dieser Symbolische Link sorgt dafür, dass Programme, die den absoluten Pfad zum User Verzeichnis suchen nicht auf der SSD danach suchen, sondern vom System automatisch auf die interne HDD umgeleitet werden. Somit erspart man sich überall entsprechende Umkonfigurationen.

Nächster wichtiger Schritt ist das Korrigieren der User Zugriffrechte. Dein gerade migrierter User benötigt volle Lese/Schreibrechte auf das User Homeverzeichnis und alle seine Inhalte. Dadurch, dass ich mich an die Hardwrk.com Anleitung gehalten habe, habe ich auch einen neuen Benutzer namens Admin angelegt, mit dem ich diese temporären Arbeiten erledigt habe. Nebeneffekt war aber, dass die Besitzrechte auf der alten HDD auf diesen temporären User umgeschrieben wurden und ich für jedes Verzeichnis meines eigentlichen Users die Rechte neu setzen musste. Dazu wählt man Informationen aus, wenn man auf den Userordner einen Rechtsklick macht. In dem erscheinenden Fenster gibt es ganz unten einen Punkt namens  "Freigabe & Zugriffsrechte". Hier sollten  "staff, nur lesen" und  "everyone, nur lesen" sowie der Name des temporären Users mit  "Lesen & Schreiben" stehen. Ein Klick auf das kleine Vorhängeschloss fragt den Benutzer nach seinem Passwort, da man Systemeinstellungen jetzt verändert. Ein Klick auf das Pluszeichen führt zu einem Fenster, wo man seinen migrierten User auswählen kann. Dieser User bekommt jetzt noch  "Lesen & Schreiben" als Zugriffsrecht verpasst. Ein Klick auf das Zahnradsymbol neben dem Plus- und Minuszeichen erlaubt den Zugriff auf die Funktion  "auf alle Unterobjekte anwenden...". Dieser Vorgang dauert je nach Umfang des Verzeichnisses entsprechend lange, sorgt aber dafür, dass alle Rechte entsprechend richtig gesetzt sind und der migrierte User wieder Besitzer der Dateien und Ordner wird. Der temporär angelegte User kann nun gelöscht werden

Glückwunsch, wenn bis hierhin alles funktioniert hat! Jetzt kann man von der alten internen HDD noch alle Ordner außer dem Benutzer Verzeichnis löschen und hat somit die komplette alte Installation von Mac OS X entfernt. Dies solltet ihr natürlich nur dann machen, wenn ihr euch sicher seid, dass ihr den Inhalt nicht mehr benötigt.

**Fazit:**  
Was hat mir das ganze jetzt eigentlich gebracht? Nun, der Mac fühlt sich deutlich flüssiger und angenehmer an. Die mich nervenden Wartezeiten sind jetzt vorbei, ich kann mehrere Programme gleichzeitig auf machen und auch offen halten, ohne das meine Festplatte die CPU die ganze Zeit ausbremst. Natürlich sind nur die Sachen von der SSD wirklich schneller geworden, die Userdaten an sich liegen ja nach wie vor auf der HDD. Hier kann man sicherlich noch in den nächsten Wochen ausprobieren, was denn das auslagern einzelner Ordner auf die SSD bringt und wie sich das im normalen Arbeitsalltag auswirkt. Abschließend gibt es jetzt noch ein paar Fotos, u.a. auch die Ergebnisse von [Xbench](http://www.xbench.com/).

<div id='gallery-1' class='gallery galleryid-1559 gallery-columns-3 gallery-size-thumbnail'>
  <figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd1.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd1-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd2.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd2-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd3.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd3-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd6.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd6-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd7.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd7-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/ssd8.jpg' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/ssd8-290x290.jpg" class="attachment-thumbnail size-thumbnail" alt="" loading="lazy" /></a>
  </div></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://centurio.net/wp-content/uploads/2011/05/SSD_Speedvergleich.png' title="" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-1"><img width="290" height="290" src="https://centurio.net/wp-content/uploads/2011/05/SSD_Speedvergleich-290x290.png" class="attachment-thumbnail size-thumbnail" alt="Links die SSD, rechts die HDD" loading="lazy" /></a>
  </div></figure>
</div>