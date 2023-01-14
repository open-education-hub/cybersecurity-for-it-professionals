## Principiul celui mai mic privilegiu

Principiul **Least Privilege** este un efort de a limita impactul pe care o problemă de securitate îl poate avea.
Un subiect nu trebuie să dețină mai multe drepturi decât are nevoie.
Din contră, un subiect trebuie să aibă cele mai mici privilegii posibile care în același timp îi permite subiectului să își desfășoare activitățile.
Un subiect poate fi o persoană, un program, un sistem sau orice componentă a unei entități.

Ideea de bază este că dacă acel subiect este compromis, impactul va fi redus la activitățile pe care le poate efectua subiectul.
Dacă respectivele acțiuni sunt limitate, tot atât de limitat va fi și impactul de securitate.

Nu există un mod unic pentru a implementa corect acest principiu.
Există doar mai multe modalități de a aplica diferite restricții și reguli asupra unor subiecți.

### Activități practice

Intrați în directorul `support/least-privilege/` și parcurgeți exercițiile de mai jos.

1. Accesați directorul `maze/remote/` și rulați comanda `make run`.
   Comanda va lansa în execuție un container `Docker` aferent challenge-ului `maze`.
   Containerul va expune un serviciu `SSH` pe portul 10222.

   Seturile de credențiale pe care le vom folosi pe parcursul exercițiului curent sunt:

   - `alice:Alic3Pass`
   - `bob:Boy0Boy`
   - `carl:Carlit0s`

   Scopul exercițiului este de a arăta că **managementul accesului** este o activitate ce devine mai complexă pe masură ce avem din ce în ce mai mulți utilizatori pe sistem.

   Obiectivul este citirea fișierului `/home/ctf/secret` ce în mod normal nu este accesibil tuturor.
   Însă în procesul de configurare a accesului, unuia dintre utilizatori i s-a dat access la acel fișier.

   Descoperiți care dintre utilizatori poate citi conținutul fișierului `/home/ctf/secret` și aflați conținutul lui.

   Cea mai rudimentară variantă este să ne conectam pe rând cu fiecare utilizator și să vedem dacă există drepturi de citire pe acel fișier.

   Pentru aceasta, se vor folosi comenzile:

   ```
   ssh alice@0.0.0.0 -p 10222
   ssh bob@0.0.0.0 -p 10222
   ssh carl@0.0.0.0 -p 10222
   ```

   Care este motivul pentru care un anumit utilizator poate vedea conțintul fișierului `/home/ctf/secret`?
   Enumerați și alte variante prin care se poate ajunge la rezultatul dorit.
   
   Testați concluziile exercițiului și la adresa `141.85.224.104:10222`.

### Quiz

[Quiz](../quiz/least-privilege.md)
