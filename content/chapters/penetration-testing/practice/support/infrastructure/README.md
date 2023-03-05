# Infrastructura de test

În laboratorul curent vom ataca alte mașini virtuale.
Însă acest lucru trebuie executat în siguranță.

Mașinile atacate sunt vulnerabile în mod intenționat.
Expunerea acestor vulnerabilități către exterior ar fi o mare breșă de securitate.

Un prim pas în securizarea modului de lucru îl reprezintă însăși folosirea unor mașini virtuale.
Cel de al doilea pas este izolarea la nivelul rețelei.
Mașinile vulnerabile sunt conectate strict la mașina atacator.

Foarte important este să nu conectăm astfel de mașini la internet.
Deși majoritatea rețelelor în care ne aflăm nu ies *direct* în Internet, chiar și expunerea în rețeaua locală poate fi uneori un mare risc.

Folosirea `VirtualBox` cu un adaptor de rețea tip `Host-only Adapter` asigură că mașina virtuală nu poate trimite pachete decât mașinii atacotor.
Din moment ce mașina atacator este `Kali Linux` și nu are optiunea de a forwarda pachete, mașina vulnerabilă nu poate comunica cu alte mașini.
