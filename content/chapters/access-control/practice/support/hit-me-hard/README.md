# Hit Me Hard

Elevarea privilegiilor presupune să pornim de la un utilizator neprivilegiat.
Prin exploatarea anumitor mecanisme sau a unor greșeli de configurare, se poate ajunge la a executa comenzi cu drepturi elevate.

Se presupune că deja avem acces neprivilegiat la sistem.
Pentru a accesa sistemul, folositi `ssh` pentru a va loga pe stația `141.85.224.104` pe portul `10202`.
Credențialele sunt `ctf:hit-me-hard-0`.

Comanda completa pentru a accesa sistemul este:

```
ssh ctf@141.85.224.104 -p 10202
```

Obiectivul este aflarea oricăror informații ne-ar ajuta să ajungem la conținutul restricționat al fișierului `flag`.

În primul rând, să ne reamintim modul în care sistemele Unix gestionează permisiunile:

```
$ ls -l flag
-r-------- 1 root ctf 32 Oct  5 12:57 flag
```

Permisiunile sunt configurate explicit ca doar userul `root` să poată citi fișierul `flag`.
De aici concluzia că are un conținut ce nu ar trebui accesat în mod neprivilegiat.
Asta înseamnă și că pentru un atacator este o țintă bună.

Totuși, sistemele au multiple mecanisme de gestionare a permisiunilor.
Unul dintre acestea sunt **capabilitățile**.

Folosiți utilitarul `getcap` pentru a descoperi toate binarele ce au asociate capabilități.
