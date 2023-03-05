# Metasploit tutorial

Pentru a lansa Metasploit folosiți comanda:

``` shell
msfconsole
```

Sistemul de operare Kali Linux vine cu Metasploit instalat, deci nu va fi nevoie de instalare.

Una dintre cele mai folositoare comenzi este `search`.

De exemplu, pentru a căuta vulnerabilități cunoscute in software-ul `vsftpd` se folosește:

``` shell
> search vsftpd

Matching Modules
================

   #  Name                                  Disclosure Date  Rank       Check  Description
   -  ----                                  ---------------  ----       -----  -----------
   0  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  No     VSFTPD v2.3.4 Backdoor Command Execution


Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/ftp/vsftpd_234_backdoor
```

Pentru a alege un modul (modulele sunt exploit-uri), folosiți comanda `use`:

``` shell
> use 0
[*] Using configured payload cmd/unix/interact
msf6 exploit(unix/ftp/vsftpd_234_backdoor) >
```

Comanda `info` afișează o descriere a modulului ales.
Comanda `show options` detaliază parametrii modulului curent.

Dintre aceștia, cei mai utili sunt:

- `rhosts` specifică IP-urile țintă
- `lhost` specifică IP-ul mașinii atacatorului
- `payload` specifică modului care va fi livrat și executat pe țintă (de obicei un **reverse shell**)
