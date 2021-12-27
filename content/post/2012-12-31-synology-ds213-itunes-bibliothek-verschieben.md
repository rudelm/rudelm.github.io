---
author: Centurio
categories:
- Apple
- NAS
date: "2012-12-31T18:16:32Z"
guid: http://centurio.net/?p=2032
id: 2032
image: /wp-content/uploads/2012/12/IMG_1291.jpg
tags:
- DS213+
- itunes
- Synology
title: Synology DS213+ &#8211; iTunes Bibliothek verschieben
url: /2012/12/31/synology-ds213-itunes-bibliothek-verschieben/
---
Neben meinen Bildern möchte ich eigentlich auch meine Musik zentral auf der DS vorhalten. Verschiedene Anleitungen habe ich ausprobiert und bin letztlich bei einer ganz einfachen Lösung hängen geblieben. Wichtig ist natürlich: <span style="color: #ff0000;">Macht ein Backup eurer Datenbank bevor ihr die Experimente macht 😉</span>

&nbsp;

Viele Anleitungen aus dem [Synology](http://www.synology-forum.de/showthread.html?24475-iTunes-Mediathek-auslagern/page25)&#8211;[Forum](http://www.synology-forum.de/showthread.html?24475-iTunes-Mediathek-auslagern/page21) und -Wiki schlagen die Erstellung einer komplett neuen Library vor. Dabei verliert man allerdings alle Meta Informationen und Playlisten. Hier hlefen auch Tools wie Tune-Instructor nicht mehr weiter. Bei mir fehlten dann z.B. sehr viele Cover oder die Jahrelang gepflegten Playlisten.

&nbsp;

Am besten hat mir [diese Anleitung](http://www.ilounge.com/index.php/articles/comments/moving-your-itunes-library-to-a-new-hard-drive/) geholfen. Ich habe mein iTunes so eingestellt, das es sich komplett um die Verwaltung der Inhalte kümmern soll. Dies ist auch zwingend erforderlich, denn nur so kann man garantieren, dass auch alle Dateien auf das NAS korrekterweise übertragen werden.

  1. Erstellt ein Backup.
  2. Stellt in den iTunes Einstellungen einen neuen Pfad für das iTunes Media Verzeichnis ein. Ich verwende bei mir innerhalb des DS music Ordner den folgenden Pfad: music/iTunes/iTunes Media
  3. Jetzt muss man iTunes neu organisieren lassen. Dazu geht man auf Ablage, Mediathek, Mediathek organisieren.
  4. Wähle &#8222;Dateien zusammenlegen&#8220; aus. Damit werden alle von iTunes gerade verwalteten Objekte in den neuen iTunes Media Ordner kopiert.
  5. Wenn iTunes fertig ist, so kann man überprüfen ob alles funktioniert und vorhanden ist. Wenn man sich die Informationen eines Objekts anguckt, so sollte dort der neue Pfad sichtbar sein.
  6. Man kann jetzt den alten iTunes Media Ordner von der lokalen Festplatte löschen.

Es sind bei mir alle Dateien mit allen Metainformationen und Playlisten erhalten geblieben.