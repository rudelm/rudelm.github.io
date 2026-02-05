---
author: Centurio
categories:
- NAS
date: "2012-12-29T20:42:27Z"
guid: http://centurio.net/?p=2021
id: 2021
image: /2012/12/22/synology-ds213-raid-1-oder-shr/images/DS213plus.jpg
tags:
- DS213+
- Mac OS X
- SSH
- Synology
title: Synology DS213+ - SSH mit Zertifikaten

---
## Einleitung
Auf der Synology DS213+ läuft ein Linux System. Dies kann man manchmal am bequemsten per Konsole über SSH steuern. Dabei hat man entweder die Möglichkeit eine User/Passwort Kombination oder eine User/Zertifikat Kombination zum Authentifizieren zu verwenden. Letztere ist deutlich sicherer und auch bequemer. Ich möchte daher kurz meine eigene Version der notwendigen Schritte bloggen, da die [meisten](https://confluence.atlassian.com/pages/viewpage.action?pageId=271943168#ConfiguringMultipleSSHIdentitiesforGitBash,MacOSX,&Linux-CreatemultipleidentitiesforMacOSX,GitBash,andLinux) verfügbaren Anleitungen nicht alle Schritte optimal für meine Situation lösen. Daher bekommt ihr hier jetzt meine Vorgehensweise, die teilweise Befehle aus den verlinkten Anleitungen nutzt:
 
### Aktivieren des SSH/Telnet Dienstes auf der DS

Systemsteuerung, Terminal, Haken bei beiden Diensten setzen. Telnet machen wir im Moment nur an, damit wir im Notfall per Telnet uns auf die Konsole anmelden können. Dieser Dienst sollte nach erfolgreicher Konfiguration wieder dringend geschlossen werden, da die Daten unverschlüsselt übertragen werden!

### Einloggen mittels SSH

Ich gehe mal davon aus, das jeder schon einmal SSH verwendet hat. Wenn nicht, dann gibt es z.B. [hier eine gute Anleitung](http://wiki.ubuntuusers.de/SSH). Ich selber nutze Mac OS X, daher bezieht sich diese Anleitung auch nur auf Mac OS X, sollte aber mit jedem Linux ähnlich machbar sein. Windows User mögen an dieser Stelle sich über [Putty](http://www.putty.org/) informieren.

Als User verwendet man root mit dem Passwort des DiskStation admin Benutzers.


### SSH Key generieren

Mit dem Befehl

```
ssh-keygen -t rsa
```

wird ein SSH Schlüsselpaar auf der DS erzeugt. Dieses ist dann gültig für den root User. Man kann diesen Schritt aber auch für einzelne Benutzer anlegen, wenn man denn vorher unter Systemsteuerung, Benutzer, Benutzerbasis den Benutzer-Home-Dienst aktiviert hat. Damit erhält dann jeder Benutzer ein eigenes home Verzeichnis, indem dann z.B. die SSH Keys abgelegt werden können.

Bei der Erzeugung wird man nach einem Passwort gefragt. Dieses Passwort wird verwendet, um das Zertifikat vor unbefugter Benutzung zu schützen. Meine Empfehlung: Definitiv eins setzen. Man muss es dann jedes Mal vor der Verwendung des Schlüssels eingeben (es sei denn, man speichert es, aber dazu später mehr).

Aus dem erzeugten Schlüsselpaar kopieren wir jetzt den öffentlichen Schlüssel in die Datei authorized_keys:

```
cat /root/.ssh/id_rsa.pub  >> /root/.ssh/authorized_keys
```

Dieser Befehl hängt den Inhalt von id\_rsa.pub an das Ende von authorized\_keys und erzeugt die Datei, falls sie noch nicht existiert. Die Datei wird jetzt vor neugierigen Blicken auf dem System geschützt, es darf  nur noch root die Datei lesen:

```
chmod 600 /root/.ssh/authorized_keys
```

Die Inhalte des privaten und des öffentlichen Schlüssels sichern wir jetzt auf eurem PC. Dazu könnt ihr am einfachsten die Inhalte mit dem cat Befehl anzeigen lassen und kopiert sie einfach aus dem Terminal in eine Datei auf eurem PC. Hier gibt es auch elegantere Methoden (mit scp rüberkopieren), aber das lasse ich im Moment um es nicht unnötig kompliziert zu machen. Kopiert den Inhalt von

```
cat /root/.ssh/id_rsa
```

in eine id\_rsa\_ds213plus Datei auf eurem System. Das Gleiche macht ihr auch für die Datei id\_rsa.pub und kopiert sie in eine id\_rsa_ds213plus.pub Datei auf eurem System:

```
cat /root/.ssh/id_rsa.pub
```

Ihr solltet jetzt zwei Dateien haben:

  * id_rsa_ds213plus - euer privater Schlüssel
  * id_rsa_ds213plus.pub  - euer öffentlicher Schlüssel

### SSH Daemon konfigurieren

Ihr müsst die Authentifizierung mit Zertifikaten erst noch aktivieren. Dies stellt ihr in der Datei sshd_config ein. Diese Datei findet ihr im Ordner /etc/ssh. Ich benutze den Editor vi. Die Bedienung des Editors erkläre ich jetzt nicht, da verweise ich auf [diese Seite](http://www.danielklicks.de/blog/2012/04/synology-disk-station-gesicherter-ssh-zugang-mit-private-key/).

Es müssen jetzt folgende drei Stellen auskommentiert bzw. hinzugefügt werden:

```
RSAAuthentication yes
```

```
PubkeyAuthentication yes
```

```
AuthorizedKeysFile ~/.ssh/authorized_keys
```

Bevor jetzt der SSH Dienst voreilig neugestartet wird, müsst ihr erst einmal auf eurem Client die Konfiguration entsprechend anpassen.

### SSH Client konfigurieren

Ihr habt im Schritt 3 zwei Dateien erzeugt mit dem Schlüsselpaar. Diese Dateien kopiert ihr euch in das .ssh Verzeichnis eures Benutzers und setzt die Rechte nur für diesen Benutzer mit dem Befehl

```
chmod 600 id_rsa_ds213plus*
```

In der Datei config legen wir jetzt eine Verbindungskonfiguration an. Falls die Datei noch nicht existiert, erzeugt sie. Die Datei soll ebenfalls im .ssh Verzeichnes des Users liegen. Ihr Inhalt sieht wie folgt aus:

```
Host ds
 HostName IP-der-DS
 Port 22
 User root
 IdentityFile ~/.ssh/id_rsa_ds213plus
```

Wenn man jetzt ssh ds als Befehl eintippen würde, so würde dein SSH Client sich zu deiner DS unter der angegebenen IP verbinden auf Port 22, mit User root und dem privaten Schlüssel den wir vorhin kopiert hatten.

### Testen

Der SSH Daemon muss neugestartet werden auf der DS. Dies geschieht mit dem Befehl

```
sh /usr/syno/etc.defaults/rc.d/S95sshd.sh restart
```

Anschließend ist deine aktive SSH Verbindung getrennt worden. Solltest du hier einen Fehler gemacht haben, so kommst du nicht mehr per SSH auf die DS. Hier kannst du dann aber die vorhin aktivierte Telnet Verbindung als Backup benutzen.

Verbinde dich erneut mit

```
ssh ds
```

Du solltest jetzt nach deinem Passwort zu dem vorhin erstellten SSH Schlüsselpaar gefragt werden. Hast du es eingegeben, so bist du direkt eingeloggt und musst nicht mehr das Passwort des DS admin verwenden.

### Aufräumen

In der config Datei des SSH Daemons kann man jetzt noch die User/Passwort Authentifizierung abschalten. Dies geschieht mit folgender Zeile:

```
PasswordAuthentication no
```

Nach einem Neustart des SSH Daemons (siehe oben) solltest du dich nur noch mit deinem SSH Schlüsselpaar anmelden können. Pass also gut auf sie auf!

Deaktiviere nun noch den Telnet Dienst in der Systemsteuerung der DS.

### Optionales

Wenn du Mac OS verwendest, so wirst du bereits bei der Eingabe des Passworts für den SSH Key das Feld zum Speichern des Passwortes bemerkt haben. Wenn du diese Option wählst, so wird das Passwort in dem Mac OS Schlüsselbund hinterlegt. Ähnliche Möglichkeiten gibt es auch für Windows und Linux. Da schau am besten in den oben verlinkten Seiten nach.