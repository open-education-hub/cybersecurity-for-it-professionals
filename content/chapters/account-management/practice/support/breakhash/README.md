### Tutorial Spargere Hash

În urma unor activități de Red Teaming, am obținut o listă de parole (`passwords`) folosite în infrastructura țintă.
Mai mult, au fost compromise și unele stații de lucru.
De pe stațiile compromise s-au obținut hashuri de parole (`hashes`).

Parolele din spatele hashurilor sunt folosite pentru logare în sisteme foarte sensibile.
Aceste sisteme permit o singură încercare de logare.
Daca parola este greșită, sistemul se blochează.

Drept urmare, trebuie să spargem hashurile.
Apoi cu parolele obținute ne putem loga mai departe în sistemele sensibile.
