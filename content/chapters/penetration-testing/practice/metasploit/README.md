# Metasploit tutorial

Metasploit is started with the following command:

``` shell
msfconsole
```

Kali has it preinstalled so there is no configuration needed.

One of the most useful commands being used is the `search` command.

For example, to search for vulnerabilities about `vsftpd` use:

``` shell
> search vsftpd

Matching Modules
================

   #  Name                                  Disclosure Date  Rank       Check  Description
   -  ----                                  ---------------  ----       -----  -----------
   0  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  No     VSFTPD v2.3.4 Backdoor Command Execution


Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/ftp/vsftpd_234_backdoor
```

To choose a module/exploit, use the `use` command:

``` shell
> use 0
[*] Using configured payload cmd/unix/interact
msf6 exploit(unix/ftp/vsftpd_234_backdoor) >
```

The `info` command reveals information about the chosen module.
The `show options` details parameters that could be changed regarding the current exploit.

The `rhosts` and `lhost` parameters are very important to be aware of.
The `rhosts` is for specifying targets.
The `lhost` is for specyfying the attacker machine.

Another important parameter is the `payload` parameter itself.
The `payload` is what gets executed on the compromised machine.
Usually, a reverse shell is what the attacker wants.
