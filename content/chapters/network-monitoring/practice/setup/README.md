# Setup

Descărcați fișierul `USO_tom_jerry.ova` de la următoarea adresă: http://vmx.cs.pub.ro/~training/

De asemenea, descărcați și instalați `VirtualBox`.

Dupa ce ați instalat `VirtualBox`, importați fisierul `tom_jerry.ova`.
În urma importării acestuia, se vor crea doua mașini virtuale, anume `tom` și `jerry`.

Cel mai probabil, la pornirea mașinilor virtuale veți primi eroarea `Could not start the machine ... because the following physical network interfaces were not found: vboxnet0`.
Pentru a rezolva această eroare, trebuie creat adaptorul `vboxnet0`.
Accesați fereastra `VirtualBox`, `File > Host Network Manager` și apăsați butonul `Create`.
Opțiunea `vboxnet0` va apărea automat.
Asigurați-vă că este selectată, după care restartați mașina virtuală.

Credențialele de acces pentru ambele mașini sunt `student:student`.

După pornirea ambelor mașini virtuale trebuie asigurată conectivitatea dintre ele.
Interfețele de rețea folosite pentru a comunica între ele sunt `enp0s8`.
Folosiți comanda `ip a sh` și veți observa că nu sunt adrese IP asignate pe aceste interfețe.
Pentru a aloca adrese IP, rulați pe ambele mașini virtuale comanda `sudo dhclient enp0s8`.

În acest moment ambele mașini virtuale ar trebui să aibă adrese IP asignate pe interfețele `enp0s8`.
Astfel, ele vor putea comunica între ele.
