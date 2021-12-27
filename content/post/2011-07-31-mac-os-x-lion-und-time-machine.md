---
author: Centurio
categories:
- Apple
date: "2011-07-31T18:13:30Z"
guid: http://centurio.net/?p=1632
id: 1632
image: /wp-content/uploads/2011/07/MobileBackups.png
tags:
- Lion
- Time Machine
title: Mac OS X Lion und Time Machine
url: /2011/07/31/mac-os-x-lion-und-time-machine/
---
Bei meiner Installation von Lion habe ich ja bereits eine merkwürdige ca. 120GB große Partition erkannt, die als Time Machine Backup definiert war. Diese Platte hieß dann auch noch MobileBackups, was mich doch irgendwie sehr gewundert hat. Was hat es mit dieser Platte auf sich? Auf dem Desktop sehe ich diese Platte nicht und Platz hat es auch nicht weggenommen.

**Update: weiter unten habe ich noch ein paar neuere Details ergänzt**

Ich habe daher erst mal gedacht, es handelt sich bei dieser Partition um irgendeinen Bestandteil von Apples neuer Versions Funktion. Allein schon der merkwürdige Name MobileBackups hatte diese Assoziation in mir geweckt. Ich habe mich jedenfalls erst einmal nicht mehr weiter damit befasst.

Doch vorgestern habe ich dann einem Freund das Phänomen gezeigt und ihn gefragt, ob er in Lion auch das Problem hätte, bzw. ob er denn diese Partition in iStat Widget sehen würde. Er verneinte natürlich, brachte mich dann aber doch auf die einfache Idee in das Volumes Verzeichnis zu wechseln und nachzuschauen, was denn überhaupt auf dem Laufwerk vorhanden ist:

<!--more-->

`<br />
centuriombp:~ rudelm$ cd /Volumes/MobileBackups/<br />
centuriombp:MobileBackups rudelm$ ls<br />
Backups.backupdb<br />
centuriombp:MobileBackups rudelm$ mount<br />
/dev/disk0s2 on / (hfs, local, journaled)<br />
devfs on /dev (devfs, local, nobrowse)<br />
map -hosts on /net (autofs, nosuid, automounted, nobrowse)<br />
map auto_home on /home (autofs, automounted, nobrowse)<br />
/dev/disk1s2 on /Volumes/HDD (hfs, local, journaled)<br />
localhost:/yHPeyyYZB98TfHAjzdSPeT on /Volumes/MobileBackups (mtmfs, nosuid, read-only, nobrowse)<br />
centuriombp:MobileBackups rudelm$ df -h<br />
Filesystem                          Size   Used  Avail Capacity  Mounted on<br />
/dev/disk0s2                       111Gi   81Gi   30Gi    74%    /<br />
devfs                              186Ki  186Ki    0Bi   100%    /dev<br />
map -hosts                           0Bi    0Bi    0Bi   100%    /net<br />
map auto_home                        0Bi    0Bi    0Bi   100%    /home<br />
/dev/disk1s2                       465Gi  263Gi  202Gi    57%    /Volumes/HDD<br />
localhost:/yHPeyyYZB98TfHAjzdSPeT  111Gi  111Gi    0Bi   100%    /Volumes/MobileBackups<br />
` 

Interessant! Es handelt sich also echt um ein Time Machine Verzeichnis. Und in den Mount Optionen wurde auch explizit angegeben, dass es read only und nicht durchsuchbar sein sollte. Außerdem zeigt die Quelle von /Volumes/MobileBackups auf einen Pfad auf meinem System (localhost:/yHPeyyYZB98TfHAjzdSPeT).

Und nachdem ich dann auch das Time Machine Verzeichnis gesehen hatte und die Größe der Platte (120GB) in Verbindung gesetzt hatte, fiel es mir auch wieder ein! Ich hatte noch unter Snow Leopard eine kleine externe 2,5" 120GB USB Festplatte als Time Machine Volume konfiguriert. Nur angeschlossen habe ich es seit Lion nicht mehr! Dazu passt dann auch das ständige Ausrufezeichen in der Menüzeile:

<a href="http://centurio.net/wp-content/uploads/2011/07/TimeMachineVerzoegert.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/07/TimeMachineVerzoegert.png" alt="" title="Time Machine Verzoegert" width="342" height="169" class="aligncenter size-full wp-image-1633" srcset="https://centurio.net/wp-content/uploads/2011/07/TimeMachineVerzoegert.png 342w, https://centurio.net/wp-content/uploads/2011/07/TimeMachineVerzoegert-300x148.png 300w" sizes="(max-width: 342px) 100vw, 342px" /></a>

Normalerweise sichere ich auf einer Firewire 800 Festplatte. Ich vermute allerdings, dass Time Machine noch irgendwo noch einen Restlichen Bestandteil er 120GB Festplatte registriert hat und darauf wartet, dass dieses Volume wieder angeschlossen wird. Jedoch ist diese kleine Festplatte auch gar nicht geeignet, alle meine Daten aufzubewahren, weswegen ich jetzt doch ganz gerne diesen unnötigen Mount entfernen möchte.

Ein einfaches `sudo umount /Volumes/MobileBackups/` hat dann auch gereicht um diesen Time Machine Rest zu entfernen:

`centuriombp:Volumes rudelm$ sudo umount /Volumes/MobileBackups/<br />
Password:<br />
centuriombp:Volumes rudelm$ mount<br />
/dev/disk0s2 on / (hfs, local, journaled)<br />
devfs on /dev (devfs, local, nobrowse)<br />
map -hosts on /net (autofs, nosuid, automounted, nobrowse)<br />
map auto_home on /home (autofs, automounted, nobrowse)<br />
/dev/disk1s2 on /Volumes/HDD (hfs, local, journaled)<br />
centuriombp:Volumes rudelm$ ls<br />
HDD	SSD<br />
` 

Jetzt zeigt mit weder Mount noch das iStat Widget dieses merkwürdige Time Machine Volume an. Interessant war an der ganzen Sache nur, dass diese Partition mit 120GB Daten gefüllt war und auch tatsächlich auslesbare Dateiinhalte besaß. Ich vermute mal, dass bei der Lion Upgrade Installation irgendwie ein fehlerhafter oder veralteter Eintrag für Time Machine aktiviert wurde. Hoffentlich ist das Backup auf der Firewire Platte wenigstens in Ordnung. So wirklich testen lässt sich das ja nicht. Man kann höchstens mit dem Festplattenverwaltungsprogramm das Dateisystem überprüfen lassen oder aber Time Machine in einem gesicherten Ordner starten und gucken, ob Veränderungen mit gesichert wurden. 

**Update:**  
Hm, ich habe mich wohl doch geirrt. Die 2,5" Festplatte heißt doch nicht MobileBackups sondern 2ndBackups 🙂 Aber die Größe passte wunderbar zu der externen Festplatte. Nach einigen Tweets mit [@rsobik](http://www.twitter.com/rsobik) haben wir dann doch rausgefunden, dass es sich um die neue lokale Time Machine Datenbank für mobile Apple Rechner handelt. John Siracusa hat in [seinem Ars Technica Bericht](http://arstechnica.com/apple/reviews/2011/07/mac-os-x-10-7.ars/18) noch nähere Details zu der neuen Time Machine. Es wird lokal ein NFS Server gestartet, zu dem sich dann das Mobile Time Machine verbindet. Das ist dann der merkwürdige Eintrag in mount mit localhost gewesen. Bisher habe ich noch nicht dieses MobileBackup wieder aktivieren können. Ich vermute mal, dass erst nach einem Neustart das Volume wieder angelegt wird. Ein einfaches fehlendes Time Machine Backup löst jedenfalls nicht das automatische Anlegen dieses Volumes aus. Wer übrigens Probleme mit diesem Backup hat, kann dieses mit `sudo tmutil disablelocal` deaktiveren. [Jan Münnich](http://www.jan-muennich.de/lion-mobile-backup-lokale-time-machine-abschalten) hatte da z.B. Probleme mit seiner SSD und musste die Backups daher abschalten. Die MobileBackups sollen übrigens in /.MobileBackups liegen, da liegt bei mir aber nichts. Vielleicht taucht es ja die Tage erneut nach einem Neustart mal wieder auf. 120GB ist auch die Größe meiner SSD, vielleicht wird dann da entsprechend auch was drauf angelegt. Wie dem auch sei, man muss das Ganze mal weiter beobachten.

**Update 2:**  
Aha, da haben wir das ganze also wieder: Man muss `sudo tmutil enablelocal` eintippen, dann einmal Time Machine versuchen zu starten. Es sucht dann nach einem verfügbaren Backup Volume, findet aber natürlich nichts (setzt natürlich abgeklemmte Time Machine Platte voraus). Jetzt wird wieder in /.MobileBackups eine lokale Time Machine Kopie erstellt, die dann auch wieder über Mount sichtbar wird. Interessanterweise habe ich jetzt im iStat Widget auch den komischen Volumenamen, den auch Daniel Stødle [hier](http://www.scsc.no/blog/2011/07-25-the-volumesmobilebackups-directory.html) beschrieben hat. Vorher zeigte mir das Widget immer MobileBackups an, statt dessen orientiert es sich jetzt an dem kryptischen NFS Namen zu dem sich das lokale Time Machine jetzt verbindet. In /Volumes/MobileBackups befindet sich dann die gemountete backups.db Datenbank von Time Machine. Die 120GB erklären sich damit auch von alleine. Da das Backup Verzeichnis auf der Systemplatte in /.MobileBackups angelegt wird, wird auch die Größe der Systempartition verwendet. In meinem Fall 120GB auf der SSD. Die Partition wird allerdings als komplett gefüllt angezeigt mit 0 Bytes freiem Speicherplatz. Ich hoffe jetzt aber, dass Time Machine mir nicht meine SSD noch weiter zu müllt und dass es ordnungsgemäß beim Anschließen des Time Machine Volumes alles von der SSD entfernt bzw. überträgt.

**Update 3:**  
Also [dieser Artikel](http://web.me.com/pondini/Time_Machine/30.html) fasst es bisher am besten zusammen: Demnach werden lokale Time Machine Backups erst nach einer Zeit gelöscht oder alternativ, wenn kein Platz mehr lokal auf der Partition vorhanden ist. Ich finde das irgendwie unschön und hätte gerne, dass das lokale Backup beim Anschließen der externen Festplatte übertragen wird und lokal gelöscht wird. So hat man dann wieder den Platz für neue lokale Backups oder für andere Sachen. Übrigens kann man lokale Backups daran erkennen, dass sie in Time Machine grau hinterlegt sind, während die eigentlichen Time Machine Backups rosa gekennzeichnet sind:

<a href="http://centurio.net/wp-content/uploads/2011/07/TimeMachineUnterschiede.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title=""><img loading="lazy" src="http://centurio.net/wp-content/uploads/2011/07/TimeMachineUnterschiede.png" alt="" title="Time Machine Unterschiede" width="140" height="273" class="aligncenter size-full wp-image-1642" /></a>