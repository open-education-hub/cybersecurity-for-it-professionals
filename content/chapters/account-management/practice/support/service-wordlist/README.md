### Wordlist VS SHH/FTP

În urma unor activități de Red Teaming, am obținut o listă de parole (`passwords.txt`) folosite în infrastructura țintă.
De asemenea, avem și o listă de useri (`users.txt`) pe care i-am întâlnit în infrastructură, pe diferite stații de lucru.

Scopul este încercarea tuturor combinațiilor posibile contra unor servicii din rețea.
Acest proces poartă denumirea de **Credentials spraying** și adesea poate obține rezultate impresionante.

Folositi utilitarul `hydra` pentru a ataca serviciul `ssh` disponibil pe portul `20003`.
