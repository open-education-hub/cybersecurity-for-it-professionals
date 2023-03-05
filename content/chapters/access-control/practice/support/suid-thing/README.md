# SUID thing

Se presupune că deja avem acces neprivilegiat la sistem.
Pentru a accesa sistemul, folositi `ssh` pentru a va loga pe stația `141.85.224.104` pe portul `30103`.
Credențialele sunt `ctf:not-what-you-expect`.

Observam că fișierul `flag` este inaccesibil.

Un alt mecanism de gestionare a privilegiilor pe sistemele Unix este cel reprezentat de `SUID`.
Este un bit special ce extinde mecanismul clasic de permisiuni din Unix.

Cu acest bit setat pe un binar, binarul va fi lansat in executie cu dreptul `ownerului` (adica proprietarul binarului).
Dacă acest proprietar este `root`, efectele pot fi catastrofale.
