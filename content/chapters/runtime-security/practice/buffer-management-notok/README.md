# Buffer Management NOT OK

Exercițiul curent exemplifică un mod incorect de gestionare a bufferului.

Similar cu exercitiul anterior, pentru un numar redus de caractere citite de la tastatura, programul se comporta la fel.

Însă atunci când se trimit mai mult de 4 octeți, programul poate avea un comportament nedefinit.

Folosiți comanda `make` pentru a compila executabilul.
Apoi lansați executabilul în executie și trimiteți pe rând urmatoarele inputuri:

- `wxyz`
- `ABCDEFGH`

Observați rezultatele rulărilor:

``` shell
$ ./buffer-management-notok
a (initial): abcd
b (initial): 0

Read some value into variable a:
wxyz

a (final): wxyz

b (final): 0
```

``` shell
$ ./buffer-management-notok
a (initial): abcd
b (initial): 0

Read some value into variable a:
ABCDEFGH

a (final): ABCDEFGH
b (final): 4736838
```
