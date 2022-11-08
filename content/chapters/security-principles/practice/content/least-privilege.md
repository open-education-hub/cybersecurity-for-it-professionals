## Principiul celui mai mic privilegiu

Principiul **Least Privilege** este un efort de a limita impactul pe care o problema de securitate il poate avea.
Un subiect nu trebuie sa detina mai multe drepturi decat are nevoie.
Din contra, un subiect trebuie sa aiba cele mai mici privilegii posibile care in acelasi timp ii permite subiectului sa isi desfasoare activitatile.
Un subiect poate fi o persoana, un program, un sistem sau orice componenta unei entitati.

Ideea de baza este ca daca acel subiect este compromis, impactul va fi redus la activitatile pe care le poate efectua subiectul.
Daca respectivele atiuni sunt limitate, tot atat de limitat va fi si impactul de securitate.

Nu exista un mod unic pentru a implementa corect acest principiu.
Exista doar mai multe modalitati de a aplica diferite restrictii si reguli asupra unor subiecti.

### Activitati practice

Intrati in directorul `support/least-privilege/` si parcurgeti exercitiile de mai jos.

1. Accesati directorul `maze/remote/` si rulati comanda `make run`.
   Comanda va lansa in executie un container `Docker` aferent challenge-ului `maze`.
   Containerul va expune un serviciu `SSH` pe portul 10222.

   Seturile de credentiale pe care le vom folosi pe parcursul exercitiului curent sunt:

   - `alice:Alic3Pass`
   - `bob:Boy0Boy`
   - `carl:Carlit0s`

   Scopul exercitiului este de a arata ca **managementul accesului** este o activitate ce devine mai complexa pe masura ce avem din ce in ce mai multi utilizatori pe sistem.

   Obiectivul este citirea fisierului `/home/ctf/secret` ce in mod normal nu este accesibil tuturor.
   Insa in procesul de configurare a accesului, unuia dintre utilizatori i s-a dat access la acel fisier.

   Descoperiti care dintre utilizatori poate citi continutul fisierului `/home/ctf/secret` si aflati continutul lui.

   Cea mai rudimentara varianta este sa ne conectam pe rand cu fiecare utilizator si sa vedem daca exista drepturi de citire pe acel fisier.

   Pentru aceasta, se vor folosi comenzile:

   ```
   ssh alice@0.0.0.0 -p 10222
   ssh bob@0.0.0.0 -p 10222
   ssh carl@0.0.0.0 -p 10222
   ```

   Care este motivul pentru care un anumit user poate vedea contintul fisierului `/home/ctf/secret`
   Enumerati si alte variante prin care se poate ajunge la rezultatul dorit.
   
   Testati concluziile exercitiului si la adresa `141.85.224.104:10222`.

### Quiz

[Quiz](../quiz/least-privilege.md)
