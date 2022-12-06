# Captures

Exercițiile curente implică găsirea unor string-uri secrete și extragerea lor dintr-o captură de rețea.
Capturile de rețea sunt in format `.pcap` și cresc in complexitate.
Scopul este să arătăm cât de repede crește în dificultate procesul de analiză a capturilor de rețea pe măsură ce avem din ce în ce mai mult trafic.

Cel mai folosit utilitar în acest sens este `Wireshark`.
Distribuția Kali folosită în laborator vine cu acest utilitar preinstalat.

Pentru a deschide un fisier denumit `capture.pcap` cu `Wireshark` folosiți comanda:

``` shell
wireshark capture.pcap
```

1. Folosiți utilitarul `Wireshark` pentru a găsi secretele din următoarele capturi de rețea:

- `capture.pcap`
- `capture2.pcap`
- `capture3.pcap`
