## Studii de caz: persoane

În continuare vom prezenta exemple reale de **vectori de atac** folosiți împotriva indivizilor.

Pentru mai multe exemple, puteți consulta rapoartele anuale ale companiilor specializate din industrie, precum Verizon `DBIR`.

### USB stick în parcare

Un studiu publicat în anul 2016 a arătat că cel puțin 48% din USB stick-urile aruncate într-un campus au fost introduse într-un PC.

Studiul se poate găsi aici:

- [Users Really Do Plug in USB Drives They Find - elie.net](https://elie.net/publication/users-really-do-plug-in-usb-drives-they-find/)

Folosirea fără control a unui stick USB poate duce la efecte nedorite și un puternic impact de securitate.
Nivelul poate fi unul personal sau se poate lărgi până la a afecta securitatea unei instituții sau firme.

### Exploatarea naivității (vishing, phishing, emailuri malițioase)

Poate compania țintă nu poate fi exploatată.
Dar poate operatorul de telefonie cu care lucrează compania țintă are probleme cu unele proceduri.
Naivitatea umană poate fi exploatată și în felul acesta se obțin informații de la operatorul call center.

Acest atac este tot o formă de [supply chain attack](https://en.wikipedia.org/wiki/Supply_chain_attack) și [phishing](https://en.wikipedia.org/wiki/Phishing).

Accesați următorul clip care arată cum anume funcționează un proces de vishing:

- [Hacking challenge at DEFCON](https://www.youtube.com/watch?v=fHhNWAKw0bY)

În clip se observă următoarele:

- atacatorul impersonează partenera victimei prin telefonul victimei
- obține adresa de email asociată cu contul
- obține acces la contul din bancă
- schimbă parola contului

În cea de a doua situație se observă cum un email de phishing poate duce la distrugerea unei vieți.
Este recomandată precauția în astfel de cazuri.
Atașamentele nu ar trebui utilizate fară o verificare prealabilă.

În cadrul instituției, se recomandă transmiterea de fișiere în mod arhivat.
Arhiva ar trebui să fie protejată prin parolă, iar parola transmisă pe alt canal (Whatsapp, SMS, etc.).

Nu descărcați utilitare de la adrese pe care nu le cunoașteți.

Verificați URL-uri să nu fie similare, precum `www.mycompany.ro` și `www.mycompamy.ro`.
Cele două site-uri arată identic din punct de vedere vizual.

În situații de acest tip, cel mai probabil un atacator încearcă să efectueze un atac de tip Phishing.
Utilizatorii care nu sunt suficient de atenți vor introduce date în cel de la doilea site.
Atacatorul va primi credențialele și le va putea utiliza în continuare.

### Schimbarea cartelei SIM

Se poate păstra numărul de telefon și schimba doar cartela SIM.
Această procedură trebuie făcută doar cu acordul deținătorului abonamentului (sau al cartelei în sine).
Totuși, unele companii nu au pusă la punct procedura aceasta și uneori se poate face de la distanță.

Accesați următorul articol pentru a vedea cum o persoană cunoscută în mediul online a fost victima unui astfel de atac:

- [This SIM card scam once fooled Jack Dorsey—here’s how to avoid it](https://www.cnbc.com/2022/02/19/how-to-avoid-sim-card-scam-that-once-fooled-jack-dorsey.html)

În România, deținătorul abonamentului trebuie să se prezinte fizic într-o sucursală pentru a face acest lucru.

### Clonarea badge-urilor

Există un trend prin care dimineața și seara la metrou este plin de oameni cu badge-uri de acces la vedere.
Badge-urile funcționează prin RFID și este foarte simplu de captat semnalul.
Este de asemenea foarte simplu de clonat acest badge.

Este o formă de **replay attack** (refolosirea unui mesaj interceptat în prealabil pentru a declanșa o funcționalitate în cadrul unui sistem).

În articolul următor se observă cât de ușor se poate clona un card de acces:

- [How to clone a security badge in seconds](https://www.youtube.com/watch?v=cxxnuofREcM)
