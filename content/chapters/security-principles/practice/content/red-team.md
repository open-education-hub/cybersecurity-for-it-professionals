## Red Team

**Red Team** este acea echipă de specialiști care trebuie să gândească asemeni unui atacator.
Echipa este fie internă companiei în care activează, fie externă și activează la cererea companiei ce cumpară serviciile lor.
Scopul lor este să emuleze atacuri, să documenteze tot procesul și apoi să propună modalități de îmbunătățire a securității.

Este o modalitate **legală** pentru specialiști să își pună în practică cunoștințele și să ajute în același timp la securizarea diferitelor entități.

O parte din activitățile pe care **Red Team** le poate efectua sunt:

- Securitate fizică
  - Încearcă să intre în clădire, să fure dispozitive, să păcălească angajați
- Dumpster Diving
  - Caută în gunoi documente sau postit-uri cu parole
- Social Engineering
  - Phishing
  - Email-uri malițioase
- OSINT
  - Inventarierea sistemelor companiei
  - Scanarea sistemelor companiei
  - Verificare dacă emailurile companiei sunt compromise
- Exploatare activă a sistemelor
  - Utilizarea exploit-urilor publice
  - Inspecție manuală a serviciilor expuse

### Activități practice

Intrați în directorul `support/red-team/` și parcurgeți exercițiile de mai jos.

1. Accesați directorul `anonymous/remote/` și rulați comanda `make run`.
   Comanda va lansa în execuție un container `Docker` aferent challenge-ului `anonymous`.

   Containerul expune două porturi importante, și anume `10021` și `10022`.
   Portul `10021` expune serviciul `FTP` iar Portul `10022` expune serviciul `SSH`.
   Prima dată vom interacționa cu serviciul `FTP`.

   Puteți interacționa cu serviciul `FTP` folosind comanda:

   ```
   $ ftp 0.0.0.0 10021
   ```

   Serverul are funcționalitatea de `anonymous login` activată.
   Acest lucru este o practică greșită de aproape fiecare dată și trebuie evitată.
   Se poate folosi doar în cazurile în care vrem să expunem **în mod public** fișiere accesibile fără restricții.

   Pentru mai multe detalii, accesați secțiunea `What is anonymous FTP` de la următorul link:

   - [How to Use Anonymous FTP](https://www.rfc-editor.org/rfc/rfc1635.html)

   Utilizatorul `anonymous` este un utilizator limitat făcut cu scopul de a oferi acces public unor anumite resurse.
   Informația esențială din resursa indicată este că utilizatorul `anonymous` acceptă orice parola.

   Drept urmare, putem folosi următoarea succesiune de acțiuni în linie de comandă pentru a ne conecta la serverul ce rulează local:

   ```
   $ ftp 0.0.0.0 10021
   # introduceti manual: user: anonymous
   # introduceti manual: password: pass
   ```

   Rezultatul ar trebui să fie:

   ```
   Connected to 0.0.0.0.
   220 (vsFTPd 3.0.3)
   Name (0.0.0.0:long): anonymous
   331 Please specify the password.
   Password: 
   230 Login successful.
   Remote system type is UNIX.
   Using binary mode to transfer files.
   ftp>
   ```

   Pentru a lista fișierele la care avem acces, folosiți comanda `passive on` urmată de comanda `ls`.
   Rezultatul ar trebui să fie:

   ```
   ftp> passive on
   Passive mode: on; fallback to active mode: off.
   ftp> ls
   229 Entering Extended Passive Mode (|||65455|)
   150 Here comes the directory listing.
   -rw-r--r--    1 0        0              27 Oct 31 14:21 credentials.txt
   226 Directory send OK.
   ftp>
   ```

   Observăm că serverul expune fișierul `credentials.txt`.
   Deseori programatorii uită ce fișiere lasă publice și se pot ajunge la situații nedorite.

   Cum accesul la fișier este nerestricționat, acesta poate fi downloadat folosind comanda `get credentials.txt`.
   Rezultatul ar trebui să fie:

   ```
   ftp> get credentials.txt
   local: credentials.txt remote: credentials.txt
   229 Entering Extended Passive Mode (|||65437|)
   150 Opening BINARY mode data connection for credentials.txt (27 bytes).
   100% |******************************************************************************************************************************************|    27        0.42 KiB/s    00:00 ETA
   226 Transfer complete.
   27 bytes received in 00:00 (0.41 KiB/s) 
   ```

   Acum putem folosi comanda `exit` pentru a închide conexiunea cu serverul `FTP`.
   Rezultatul ar trebui să fie:

   ```
   ftp> exit
   221 Goodbye.
   ```

   Acum avem local fișierul `credentials.txt` al cărui conținut îl putem expune cu următoarea comandă:

   ```
   $ cat credentials.txt
   ```

   Rezultatul ar trebui să fie:

   ```
   $ cat credentials.txt
   ctf:anonymous-account-pass
   ```

   Cea mai des folosită sintaxă de precizare a credențialelor este de forma `username:parola`.
   Observăm că asta conține și fișierul nostru.

   Acum putem încerca să folosim credențialele pentru a ne loga prin intermediul `SSH`.
   Vom face acest lucru cu utilizatorul `ctf` și parola `anonymous-account-pass`.
   Comanda folosită este:

   ```
   ssh ctf@0.0.0.0 -p 10022
   # introducem manual parola `anonymous-account-pass`
   # introducem manual `yes` pentru a continua conectarea atunci cand suntem intrebati
   ```

   Rezultatul ar trebui să fie:

   ```
   $ ssh ctf@0.0.0.0 -p 10022
   The authenticity of host '[0.0.0.0]:10022 ([0.0.0.0]:10022)' can't be established.
   ED25519 key fingerprint is SHA256:r4/eDTkhYoYa8fgSaLMUsyQJAGsSaq+5rX2FGAB0CJc.
   This key is not known by any other names
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added '[0.0.0.0]:10022' (ED25519) to the list of known hosts.
   ctf@0.0.0.0's password: 
   Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-52-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

   This system has been minimized by removing packages and content that are
   not required on a system that users do not log into.

   To restore this content, you can run the 'unminimize' command.

   The programs included with the Ubuntu system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
   applicable law.


   The programs included with the Ubuntu system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
   applicable law.

   ctf@03ca22e3acdb:~$
   ```

   Listați conținutul fișierului `secret` disponibil la calea `/home/ctf/secret`.

   Odată ce aveți un input care funcționează corespunzator, încercați același input și la adresa `141.85.224.104:10021`.

1. Accesați directorul `pingme/remote/` și rulati comanda `make run`.
   Comanda va lansa în execuție un container `Docker` aferent challenge-ului `pingme`.
   O aplicație web minimală este expusă pe portul `10002` al mașinii locale.

   Observați că aplicația execută comanda `ping` către o adresă IP dată de utilizator.

   Putem presupune că aplicația execută într-o linie de comandă pe server următoarea comandă:

   ```
   $ ping <input>
   ```

   Unde `<input>` este orice introduce utilizatorul în câmpul din pagină.
   În consecință, un utilizator al aplicatiei **injecteaza comenzi** direct într-o linie de comandă aflată pe un server la distanță.

   Cunoscând faptul că operatorul `;` delimitează comenzi și permite rularea mai multor comenzi într-o singură linie, putem folosi `8.8.8.8; whoami` ca și input.
   În acest fel, comenzile care s-ar executa pe server conform presupunerilor noastre sunt:

   ```
   $ ping 8.8.8.8; whoami
   ```

   Validați presupunerile anterioare contra aplicației expuse pe `0.0.0.0:10002`.

   Scopul este să accesați fișierul `/secret` de pe server.
   Pentru a accesa acest fișier, folosiți utilitarul `cat` și faptul că aveți informația că fișierul căutat se află sub calea `/secret`.

   Odată ce aveți un input care funcționează corespunzător, încercați același input și la adresa `141.85.224.104:10002`.

### Quiz

[Quiz](../quiz/red-team.md)
