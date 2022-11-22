# Buffer Management segfault

Similar cu exemplele anterioare, exemplul curent va exemplifica o eroare comună pentru limbajele low-level: `segmentation fault`.

Aceasta eroare are ca și cauză fie accesarea, fie suprascrierea unei zone de memorie protejate.

Observați codul sursa și faptul că de această dată se citesc mai mulți octeți (litere) de la tastatură decât în exemplele anterioare.

Acest lucru va cauza suprascrierea `adresei de retur a funcției main`, ceea ce mai departe va cauza `instruction pointer`-ul să sară într-o zonă nepermisă de memorie.

Folositi comanda `make` pentru a compila executabilul.
Lansați executabilul creat în execuție și trimiteți 16 caractere ca și input.

Rezultatul ar trebui să fie similar cu:

``` shell
./buffer-management-segfault 
a (initial): abcd
b (initial): 0

Read some value into variable a:
ABCDEFGHIJKLMNOP

a (final): ABCDEFGHIJKLMNOP�
b (final): 1229473606
zsh: segmentation fault  ./buffer-management-segfault
```

Pentru a vedea adresa ce a cauzat eroarea, folosiți comanda: `sudo dmesg | tail -n 10`.
