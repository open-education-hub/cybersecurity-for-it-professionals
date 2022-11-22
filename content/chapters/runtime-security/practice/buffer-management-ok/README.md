# Buffer Management OK

Exercițiul curent exemplifică un mod corect de gestionare a bufferului.
Examinati codul din fisierul `buffer-management-ok.c`.

Observati ca se foloseste apelul functiei `read()` pentru a citi date intr-o variabila de tip buffer.
Pentru ca se citesc un numar mic de octeti (litere) de la tastatura, programul nu are parte de comportament nedefinit.

Folositi comanda `make` pentru a compila fisierul executabil.
Apoi lansati executabilul creat in executie si trimiteti sirul de caractere `wxyz` ca input.

Rezultatul ar trebui sa fie:

``` shell
$ ./buffer-management-ok
a (initial): abcd
b (initial): 0

Read some value into variable a:
wxyz

a (final): wxyz
b (final): 0
```
