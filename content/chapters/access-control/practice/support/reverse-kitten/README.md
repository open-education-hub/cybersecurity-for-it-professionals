# Reverse Kitten

Se presupune că deja avem acces neprivilegiat la sistem.
Pentru a accesa sistemul, folositi `ssh` pentru a va loga pe stația `141.85.224.104` pe portul `10001`.
Credențialele sunt `ctf:reverse-kitten-0`.

Observam că fișierul `flag` este inaccesibil.

Există situații când un utilizator neprivilegiat își poate eleva temporar privilegiile.
Cu alte cuvinte, poate executa o comandă cu drepturi depline.

Evident, acest lucru este posibil doar în urma configurării prelabile a acestui lucru.
Deci trebuie ca un administrator al sistemului să configureze această elevare pentru un anumit user.

Aici apare pericolul unui *misconfiguration*.

Modul uzual prin care un utilizator își poate eleva drepturile îl reprezintă `sudo`.
Cu `sudo -l` se poate vedea lista tututor comenzilor pe care utilizatorul curent le poate utiliza cu `sudo`.
Comenzile pe care utilizatorul le poate rula sunt fix cele listate de `sudo -l` și trebuiesc prefixate cu `sudo`.
