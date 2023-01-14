## Studii de caz: sisteme

În continuare vom prezenta exemple reale de  **vectori de atac** folosiți împotriva sistemelor informatice.

### Stuxnet

Malware de tip **worm**.
A fost făcut inițial pentru a ataca o anumită țintă.
Ținta erau sistemele care controlau turbine ale unei centrale nucleare.
Dintr-o eroare umană introdusă în urma unui update, s-a răspândit la un laptop al unui angajat, după care în întreaga lume.

Elemente principale:

- Răspândirea inițială se bazează pe dispozitive USB
  - stick infectat folosit greșit
- Exploituri pentru Windows
  - S-au înlănțuit mai multe exploituri de tip **zero-day** (vulnerabilitați care nu au mai fost până în acel punct folosite public, sau nu se cunosc folosiri ale ei)
  - Se estimează că au fost folosite patru exploituri de tip zero-day
  - Virusul s-a răspândit pe această cale (dispozitive de tip Windows)
  - Pe fiecare dispozitiv infectat erau instalate **rootkit-uri** (software malițios care permite conectarea de la distanță pe un dispozitiv infectat)
- Exploit pentru un driver SCADA instalat pe stații Windows
  - Driverul era produs de Siemens
  - Driverul facilita comunicația dintre Windows și dispozitive tip PLC de la Siemens
  - Virusul putea apoi altera codul de pe PLC
- Virusul controlează apoi viteza de rotație a unui motor

### WannaCry

Malware de tip Cryptoworm.
În esență se propagă ca un Vierme, și criptează date de pe țintă.
Apoi cere deținătorului dispozitivului bani pentru a primi cheia de decryptare.

![WannaCry Message]( ../media/Wana_Decrypt0r_screenshot.png "https://en.wikipedia.org/wiki/WannaCry_ransomware_attack#/media/File:Wana_Decrypt0r_screenshot.png")

Elemente principale:

- Exploit-ul **EternalBlue** facilitează propagarea virusului
  - Exploatează protocolul SMB
  - Un grup numit **The Shadow Brokers** fură de la **National Security Agency** exploitul numit **EternalBlue** și îl publică pe Internet
  - O lună mai târziu apare **WannaCry** și afectează sistemele care la acel moment nu aplicaseră deja patch-urile pe care **Microsoft** le-a publicat între timp
- Utilitarul **DoublePulsar** este un **rootkit** care se instala automat pe dispozitivele compromise
- Toate datele de pe dispozitiv erau apoi criptate și se cereau bani în Bitcoin pentru ca datele să fie decriptate
