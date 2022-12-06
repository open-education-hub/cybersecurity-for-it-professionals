# HTTP

Scopul este să arătăm de ce HTTP este considerat nesigur.
Mai precis, vom arăta cât de ușor se poate intercepta trafic în momentul în care suntem într-un loc favorabil în rețea.

În exemplul curent, presupunem că atacatorul deja are acces la rețea.
Atacatorul se poate interpune între victimă și server.
Cu alte cuvinte, vom emula un scenariu al atacului *Man-in-the-middle*.

Vom folosi mașina virtuală `tom` importată anterior.
Odată logați pe masină, porniți un proces de captură de rețea.
Porniti procesul in background folosind:

``` shell
sudo tcpdump -i enp0s3 -s 65535 -w captura.pcap &
```

Apoi accesați pagina unui exercițiu din laboratoarele anterioare folosind utilitarul `wget`:

``` shell
wget http://141.85.224.104:40002/index.php
```

Dupa ce comanda se finalizează, opriți procesul din background:

``` shell
kill %1
```

Inspectați conținutul fisierului `captura.pcap` folosind `Wireshark`, ideal dupa ce fisierul `captura.pcap` a fost copiat pe masina virtuala de Kali folosind `scp`.

Alternativ, folositi comanda `cat` în mașina virtuală `tom` pentru a valida faptul ca pagina HTML este prezentă în captura de rețea:

``` shell
cat captura.pcap
```

Observați cum folosirea HTTP aduce mari dezavantaje de confidențialitate, deci securitate.
