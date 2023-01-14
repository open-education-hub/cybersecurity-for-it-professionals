## Blue Team

**Blue Team** este analogul defensiv al **Red Team**.
În cele mai multe cazuri, este o echipă interna a companiei și mai rar o componentă externă.

Rolurile sunt variate:

- Incident Response
- Threat Hunting
- Cybersecurity Analyst
- Malware Analyst

Și lista poate continua.

De asemenea, activitățile care asigură o bună protecție a organizației sunt, dar nu se limiteaza la, următoarele:

- Monitorizarea permanenta a rețelelor
- Scanarea periodică a rețelelor
- Code review / Analiză statică a codului nou adăugat
- Analiză dinamică a codului nou adaugat
- Security Awareness

Probabil cel mai dificil efort este acela de a cunoaște, la orice moment în timp, **suprafața de atac** a companiei.
Și mai dificil este monitorizarea activă a acesteia.
Noi sisteme se adaugă, cele vechi se dezactivează.
Programe noi se adaugă, cele vechi se dezinstalează.
Actualizările pot aduce cu ele vulnerabilități, sau pot afecta componentele deja existente.

O combinație între cele două echipe poartă numele de **Purple Team** și implică specialiști cu cunoștințe și din componenta de **Red Team** cât și din cea de **Blue Team**.

Pentru mai multe detalii referitoare la atribuțiile echipelor, consultați:

- [The Difference Between Red, Blue, and Purple Teams - Daniel Miessler](https://danielmiessler.com/study/red-blue-purple-teams/)

### Promovare Cybersecurity Awareness

Unul dintre obiectivele **Blue Team** este de a promova o cultură a securității cibernetice.
Acest lucru înseamnă practici atât la nivelul individual, cât și la nivelul interacțiunii dintre individ și bunurile companiei.

În urma studiilor de caz discutate, putem afirma că următoarele bune practici ar trebui implementate:

- Se interzice folosirea dispozitivelor USB din afara companiei
- Informațiile sensibile nu se lasă pe hartie sau pe orice alt suport
  - Parolele nu se pun pe postit-uri
- Documentele sensibile se depozitează în locații sigure sau se distrug
  - Un atacator ar putea face Dumpster Diving și ar putea recupera informații
- Ascundeți badge-urile în public
- Atașamentele din emailuri se verifică înainte de a fi folosite
- URL-urile din emailuri se verifică înainte de a fi accesate

### Activități practice

1. Vrem să rezolvăm vulnerabilitatea din exercițiul `support/red-team/anonymous`.
   Scopul exercițiului este să gândim și din cealaltă perspectivă a situației.
   Vrem să ne punem în locul celor care trebuie să rezolve problema și să gândim cum ar gândi **Blue Team**.

   Primul pas este identificarea problemei, și aici avem două componente:

   - Accesul nerestricționat prin cont anonim la conținutul expus de serverul `FTP`
   - Informații sensibile disponibile în directorul expus prin `FTP`

   Observăm că cea de a doua componentă ar putea fi problematică și în situația în care accesul s-ar face prin autentificare cu credențiale valide.
   Cu alte cuvinte și în cazul în care un utilizator valid ar avea acces la informații sensibile este unul problematic.

   Conform bunelor practici de securitate cibernetică pe care le-am discutat, accesul la informațiile sensibile trebuie gestionat corespunzător.

   Drept urmare, `credentials.txt` ar trebui șters din directorul pe care îl expune serverul ftp.

   Mai mult, accesul anonim ar trebui dezactivat, dacă acest lucru este conform cu obiectivul serverului.

1. Vrem să rezolvăm vulnerabilitatea din exercițiul `support/red-team/pingme`.
   **Input Sanitization** este procesul ce trebuie aplicat oricând un utilizator introduce date într-o aplicație.
   Procesul reprezintă o filtrare a datelor după niște criterii bine definite.
   Scopul acestui proces este de a ne asigura că datele introduse de utilizator au tiparul pe care aplicația îl cere.

   Exemple de astfel de situații:

   - Când o aplicație cere un CNP.
     În acest caz, dezvoltatorii trebuie să se asigure că lungimea este de 13 caractere, că data de naștere este validă și că restul regulilor sunt respectate
   - Când o aplicație cere un număr de telefon.
     În acest caz trebuie să se respecte lungimea lui, un prefix valid al unei țări, etc.

   Analizând fișierul `support/red-team/pingme/remote/index.php` se observă că nu se execută nicio filtrare asupra datelor introduse de utilizator.

   Dezvoltatorii trebuie să presupună mereu că un utilizator va vrea să introducă date neconforme cu ce se așteaptă aplicația.

   Drept urmare, ca **Blue Team** trebuie să propunem ca datele utilizatorului să fie foarte strict verificate.
   În cazul de față, vrem ca doar inputurile de forma unei adrese IP să fie acceptate.

   Cea mai simplă modalitate de a face acest lucru o reprezintă folosirea **expresiilor regulate**.

   ![Probleme Regex](https://imgs.xkcd.com/comics/perl_problems.png "")

   Consultați fișierul `solution/blue-team/pingme/fixed.php` pentru o potențială soluție.

### Quiz

[Quiz](../quiz/blue-team.md)
