# dirb

Exemplul curent va arăta procesul de `Path Brute-forcing` sau `Path discovery` aplicat împotriva unei aplicații web.

Acest atac presupune încercarea repetata a mai multor căi în aplicație.
Scopul este descoperirea cât mai multor căi și inspectarea informațiilor expuse de ele.

Accesați `http://141.85.224.104:40000/`.
Pagina expusă este o pagină prestabilită a unui server web de tip Apache.

Totuși, avem informații ca dezvoltatorii au uitat niște căi în aplicație.

Pentru a desfășura atacul, va trebui să instalăm următoarele pachete:

``` shell
sudo apt install dirb wordlists
```

Utilitarul `dirb` se foloseste de o listă de cuvinte pentru a încerca pe rând căi compuse din cuvintele din listă.
Pachetul `wordlists` furnizează liste de cuvinte, pentru a nu fi nevoiți să le compunem noi.
Totusi, în realitate, aceste wordlist-uri sunt compuse în funcție de ținta pe care o atacăm.
Acest lucru se face pentru a spori șansele de reușită ale unui atac.

Pentru a ataca aplicația, folosiți comanda:

``` shell
dirb http://141.85.224.104:40000/ /usr/share/dirb/wordlists/common.txt
```

Observați căile pe care le descoperă utilitarul și verificați-le pe toate.
