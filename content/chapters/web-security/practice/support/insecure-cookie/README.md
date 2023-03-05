# Insecure Cookie

Acest exemplu va arăta cum un mecanism de autentificare implementat greșit poate duce la vulnerabilitatea de Session Hijacking.
Cu alte cuvinte, vom putea să ne autentificăm ca un alt user.

Accesati `http://141.85.224.104:40101/`.
Observați că este o pagină de login ce așteaptă credentiale.

Avem informații că mecanismul de autentificare este vulnerabil.

Încercați autentificarea cu credentialele `test:test`.
Observați ce se întâmplă.

După autentificare, utilizatorul este redirectat către pagina `/auth`.

Mai mult, avem informația că utilizatorul `admin` exista și deține privilegii elevate.

Scopul este să păcălim aplicația că suntem userul `admin`.
