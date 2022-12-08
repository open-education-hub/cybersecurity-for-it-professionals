# Setup

Pentru laborator va fi nevoie de:
- Virtualbox
- Kali linux (mașină virtuală): https://www.kali.org/get-kali/#kali-virtual-machines
- Metasploitable 2 (mașină virtuală): https://sourceforge.net/projects/metasploitable/

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
  - Credențiale: `kali:kali`
- Mașina virtuală `Metaspoitable2`
  - Importați mașina în VirtualBox
    - Click `New` pentru a crea o nouă mașină virtuală
      - Name `metasploitable2`
      - Type `Linux`
      - Version `Other Linux 64-bit`
      - Next
    - RAM 512MB
      - Next
    - Alegeți `Use an existing virtual hard disk file`
      - Click butonul folder
      - Click `Add`
      - Navigați la hard disk-ul (fișier `vmdk`) al mașinii `metasploitable2` și apasați dublu click pe el
      - Selectați hard disk-ul adăugat și apăsați `Choose`
    - Selectați mașina virtuală `metasploitable2` din listă
      - Dublu click și alegeți `Settings`
      - Tab-ul `Network`
      - Asigurați-vă că `Adapter 1` este `Host-only Adapter` și este setat la `vboxnet0`
  - Credentiale: `msfadmin:msfadmin`
