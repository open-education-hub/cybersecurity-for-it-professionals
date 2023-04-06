# Setup

Pentru laborator va fi nevoie de:
- Virtualbox
- Kali linux (mașină virtuală): https://www.kali.org/get-kali/#kali-virtual-machines
- Kioptrix 1 (mașină virtuală): https://www.vulnhub.com/entry/kioptrix-level-1-1,22/
- VulnOS 2 (mașină virtuală): https://www.vulnhub.com/entry/vulnos-2,147/

Sunt necesare următoarele configurări:
- Adaptorul de rețea `vboxnet0` trebuie să existe
  - Fereastra VirtualBox
    - Dacă nu există, navigați la `File > Host Network Manager` și apăsați `Create`
- Mașina virtuală `Kali`
  - Importați mașina în VirtualBox
  - Selectați mașina virtuală `Kali Linux` din listă
    - Click dreapta > Settings
    - Tab-ul `Network`
      - Asigurați-vă că `Adapter 1` este `NAT`
      - Asigurați-vă că `Adapter 2` este `Host-only Adapter` și este setat la `vboxnet0`
      - Asigurați-vă că `Adapter 2`, în meniul `Advanced`, are `Adapter Type` setat la `PCnet-PCI II`
  - Credențiale: `kali:kali`
- Kioptrix 1
  - Dezarhivați arhiva descărcată
  - Deschideți fișierul `Kioptrix Level 1.vmx` într-un editor text
    - Ștergeți toate liniile care conțin `ethernet0`
  - Formatul mașinii virtuale este destinat folosirii în `VMWare`, drept urmare vom converti mașina virtuală la un format folosit de `VirtualBox`
    - Folosiți comanda `ovftool -o Kioptix\ Level\ 1.vmx Kioptix\ Level\ 1.ovf`
  - Importați mașina în VirtualBox
  - Selectați mașina virtuală `vm` din listă
    - Click dreapta > Settings
    - Tab-ul `Network`
      - Asigurați-vă că `Adapter 1` este `Host-only Adapter` și este setat la `vboxnet0`
      - Asigurați-vă că `Adapter 1`, în meniul `Advanced`, are `Adapter Type` setat la `PCnet-PCI II`
- VulnOS2
  - Dezarhivați arhiva descărcată
  - Importați mașina în VirtualBox
  - Selectați mașina virtuală `VulnOSv2` din listă
    - Click dreapta > Settings
    - Tab-ul `Network`
      - Asigurați-vă că `Adapter 1` este `Host-only Adapter` și este setat la `vboxnet0`
    - Tab-ul `USB`
      - Debifați `Enable USB Controller`
