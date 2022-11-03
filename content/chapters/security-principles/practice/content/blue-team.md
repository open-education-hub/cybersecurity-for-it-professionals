## Blue Team

**Blue Team** este analogul defensiv al **Red Team**.
De cele mai multe cazuri, este o parte interna a companiei si mai rar o componenta externa.

Rolurile sunt variate:

- Incident Response
- Threat Hunting
- Cybersecurity Analyst
- Malware Analyst

Si lista poate continua.

De asemenea, activitatile care asigura o buna protectie a organizatiei sunt, dar nu se limiteaza la, urmatoarele:

- Monitorizarea permanenta a retelelor
- Scanarea periodica a retelelor
- Code review / Analiza statica a codului nou adaugat
- Analiza dinamica a codului nou adaugat
- Security Awareness

Probabil cel mai dificil efort este acela de a cunoaste, la orice moment in timp, **suprafata de atac** a companiei.
Si mai dificil este monitorizarea activa a acesteia. Noi sisteme se adauga, cele vechi se dezactiveaza.
Programe noi se adauga, cele vechi se dezinstaleaza.
Actualizarile pot aduce cu ele vulnerabilitati, sau pot afecta componentele deja existente.

O combinatie intre cele doua echipe poarta numele de **Purple Team** si implica specialisti cu cunostinte si din componenta de **Red Team** cat si din cea de **Blue Team**.

Pentru mai multe detalii referitoare la atributiile echipelor, consultati:

- [The Difference Between Red, Blue, and Purple Teams - Daniel Miessler](https://danielmiessler.com/study/red-blue-purple-teams/)

### Promovare Cybersecurity Awareness

Unul dintre obiectivele **Blue Team** este de a promova o cultura a securitatii cibernetice.
Acest lucru inseamna practici atat la nivelul individual, cat si la nivelul interactiunii dintre individ si bunurile companiei.

In urma studiilor de caz discutate, putem afirma ca urmatoarele bune practici ar trebui implementate:

- Se interzice folosirea dispozitivelor USB din afara companiei
- Informatiile sensibile nu se lasa pe hartie sau pe orice alt suport
  - Parolele nu se pun pe postit-uri
- Documentele sensibile se depoziteaza in locatii sigure sau se distrug
  - Un atacator ar putea face Dumpster Diving si ar putea recupera informatii
- Ascundeti badge-urile in public
- Atasamentele din emailuri se verifica inainte de a fi folosite
- URL-urile din emailuri se verifica inainte de a fi accesate

### Activitati practice

1. Vrem sa rezolvam vulnerabilitatea din exercitiul `support/red-team/anonymous`.
   Scopul exercitiului este sa gandim si din cealalta perspectiva a situatiei.
   Vrem sa ne punem in locul celor care trebuie sa rezolve problema si sa gandim cum ar gandi **Blue Team**.

   Primul pas este identificarea problemei, si aici avem doua componente:

   - Accesul nerestrictionat prin cont anonim la continutul expus de serverul `FTP`
   - Informatii sensibile disponibile in directorul expus prin `FTP`

   Observam ca cea de a doua componenta ar putea fi problematica si in situatia in care accesul s-ar face prin autentificare cu credentiale valide.
   Cu alte cuvinte si in cazul in care un utilizator valid ar avea acces la informatii sensibile este unul problematic.

   Conform bunelor practici de securitate cibernetica pe care le-am discutat, accesul la informatiile sensibile trebuie gestionat corespunzator.

   Drept urmare, `credentials.txt` ar trebui sters din directorul pe care il expune serverul ftp.

   Mai mult, accesul anonim ar trebui dezactivat, daca acest lucru este conform cu obiectivul serverului.

1. Vrem sa rezolvam vulnerabilitatea din exercitiul `support/red-team/pingme`.
   **Input Sanitization** este procesul ce trebuie aplicat oricand un utilizator introduce date intr-o aplicatie.
   Procesul reprezinta o filtrare a datelor dupa niste criterii bine definite.
   Scopul acestui proces este de a ne asigura ca datele introduse de utilizator au tiparul pe care aplicatia il cere.

   Exemple de astfel de situatii:

   - Cand o aplicatie cere un CNP.
     In acest caz, dezvoltatorii trebuie sa se asigure ca lungimea este de 13 caractere, ca data de nastere este valida si ca restul regulilor sunt respectate
   - Cand o aplicatie cere un numar de telefon.
     In acest caz trebuie sa se respecte lungimea lui, un prefix valid al unei tari, etc.

   Analizand fisierul `support/red-team/pingme/remote/index.php` se observa ca nu se executa nicio filtrare asupra datelor introduse de utilizator.

   Dezvoltatorii trebuie sa presupuna mereu ca un utilizator va vrea sa introduca date neconforme cu ce se asteapta aplicatia.

   Drept urmare, ca **Blue Team** trebuie sa propunem ca datele utilizatorului sa fie foarte strict verificate.
   In cazul de fata, vrem ca doar inputurile de forma unei adrese IP sa fie acceptate.

   Cea mai simpla modalitate de a face acest lucru o reprezinta folosirea **expresiilor regulate**.

   ![Probleme Regex](https://imgs.xkcd.com/comics/perl_problems.png "")

   Consultati fisierul `solution/blue-team/pingme/fixed.php` pentru o potentiala solutie.

### Quiz

[Quiz](../quiz/blue-team.md)
