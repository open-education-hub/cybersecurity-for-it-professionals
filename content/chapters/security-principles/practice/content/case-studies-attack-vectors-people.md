## Studii de caz: persoane

In continuare vom prezenta exemple reale de **vectori de atac** folositi impotriva indivizilor.

Pentru mai multe exemple, puteti consulta rapoartele anuale ale companiilor specializate din industrie, precum Verizon `DBIR`.

### USB stick in parcare

Un studiu publicat in anul 2016 a aratat ca cel putin 48% din USB stick-urile aruncate intr-un campus au fost introduse intr-un PC.

Studiul se poate gasi aici:

- [Users Really Do Plug in USB Drives They Find - elie.net](https://elie.net/publication/users-really-do-plug-in-usb-drives-they-find/)

Folosirea fara control a unui stick USB poate duce la efecte nedorite si un puternic impact de securitate.
Nivelul poate fi unul personal sau se poate largi pana la a afecta securitatea unei institutii sau firme.

### Exploatarea naivitatii (vishing, phishing, emailuri malitioase)

Poate compania tinta nu poate fi exploatata.
Dar poate operatorul de telefonie cu care lucreaza compania tinta are probleme cu unele proceduri.
Naivitatea umana poate fi exploatata si in felul acesta se obtin informatii de la operatorul call center.

Acest atac este tot o forma de [supply chain attack](https://en.wikipedia.org/wiki/Supply_chain_attack) si [phishing](https://en.wikipedia.org/wiki/Phishing).

Accesati urmatorul clip care arata cum anume functioneaza un proces de vishing:

- [Hacking challenge at DEFCON](https://www.youtube.com/watch?v=fHhNWAKw0bY)

In clip se observa urmatoarele:

- atacatorul impersoneaza partenera victimei prin telefonul victimei
- obtine adresa de email asociata cu contul
- obtine acces la contul din banca
- schimba parola contului

In cea de a doua situatie se observa cum un email de phishing poate duce la distrugerea unei vieti.
Este recomandata precautia in astfel de cazuri. Atasamentele nu ar trebui utilizate fara o verificare prealabila.

In cadrul institutiei, se recomanda transmiterea de fisiere in mod arhivat. Arhiva ar trebui sa fie protejata prin parola, iar parola transmisa pe alt canal (Whatsapp, SMS, etc.).

Nu descarcati utilitare de la adrese pe care nu le cunoasteti.

Verificati URL-uri sa nu fie similare, precum `www.mycompany.ro` si `www.mycompamy.ro`.
Cele doua site-uri arata identic din punct de vedere vizual.

In situatii de acest tip, cel mai probabil un atacator incearca sa efectueze un atac de tip Phishing.
Utilizatorii care nu sunt suficient de atenti vor introduce date in cel de la doilea site.
Atacatorul va primi credentialele si le va putea utiliza in continuare.

### Schimbarea cartelei SIM

Se poate pastra numarul de telefon si schimba doar cartela SIM.
Aceasta procedura trebuie facuta doar cu acordul detinatorul abonamentului (sau al cartelei in sine).
Totusi, unele companii nu pus la punct procedura aceasta si uneori se poate face de la distanta.

Accesati urmatorul articol pentru a vedea cum o persoana cunoscuta in mediul online a fost victima unui astfel de atac:

- [This SIM card scam once fooled Jack Dorsey—here’s how to avoid it](https://www.cnbc.com/2022/02/19/how-to-avoid-sim-card-scam-that-once-fooled-jack-dorsey.html)

In Romania, detinatorul abonamentului trebuie sa se prezinte fizic intr-o sucursala pentru a face acest lucru.

### Clonarea badge-urilor

Exista un trend prin care dimineata si seara la metrou este plin de oameni cu badge-uri de acces la vedere.
Badge-urile functioneaza prin RFID si este foarte simplu de captat semnalul.
Este de asemenea foarte simplu de clonat acest badge.

Este o forma de **replay attack** (refolosirea unui mesaj interceptat in prealabil pentru a declansa o functionalitate in cadrul unui sistem).

In articolul urmator se observa cat de user se poate clona un card de acces:

- [How to clone a security badge in seconds](https://www.youtube.com/watch?v=cxxnuofREcM)
