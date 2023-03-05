# Metasploitable2

În acest punct, mașina virtuală `Metasploitable2` ar trebui să fie funcțională.

## Recon

Primul pas este identificarea adresei IP a mașinii virtuale țintă.

Odată ce IP-ul este descoperit, trecem la partea de **Port Scanning**.

Observați de asemenea și diferențele de output dintre cele două comenzi:

``` shell
nmap -p- <targetIP>
nmap -p- -sV <targetIP>
```

A doua comandă ar trebui să dezvăluie mult mai multe detalii, mai precis **versiuni software**.

``` text
$ nmap -p- -sV 192.168.56.104
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-08 05:50 EST
Nmap scan report for 192.168.56.104
Host is up (0.00021s latency).
Not shown: 65505 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         vsftpd 2.3.4
22/tcp    open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
23/tcp    open  telnet      Linux telnetd
25/tcp    open  smtp        Postfix smtpd
53/tcp    open  domain      ISC BIND 9.4.2
80/tcp    open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
111/tcp   open  rpcbind     2 (RPC #100000)
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
512/tcp   open  exec        netkit-rsh rexecd
513/tcp   open  login       OpenBSD or Solaris rlogind
514/tcp   open  shell       Netkit rshd
1099/tcp  open  java-rmi    GNU Classpath grmiregistry
1524/tcp  open  bindshell   Metasploitable root shell
2049/tcp  open  nfs         2-4 (RPC #100003)
2121/tcp  open  ftp         ProFTPD 1.3.1
3306/tcp  open  mysql       MySQL 5.0.51a-3ubuntu5
3632/tcp  open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
5432/tcp  open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
5900/tcp  open  vnc         VNC (protocol 3.3)
6000/tcp  open  X11         (access denied)
6667/tcp  open  irc         UnrealIRCd (Admin email admin@Metasploitable.LAN)
6697/tcp  open  irc         UnrealIRCd (Admin email admin@Metasploitable.LAN)
8009/tcp  open  ajp13       Apache Jserv (Protocol v1.3)
8180/tcp  open  http        Apache Tomcat/Coyote JSP engine 1.1
8787/tcp  open  drb         Ruby DRb RMI (Ruby 1.8; path /usr/lib/ruby/1.8/drb)
33729/tcp open  mountd      1-3 (RPC #100005)
43167/tcp open  java-rmi    GNU Classpath grmiregistry
55393/tcp open  nlockmgr    1-4 (RPC #100021)
55611/tcp open  status      1 (RPC #100024)
Service Info: Host:  metasploitable.localdomain; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 131.40 seconds
```

Mai mult, putem descoperi (cu un anumit grad de precizie) sistemul de operare folosind:

``` shell
sudo nmap -p- -O <targetIP>
```

Output-ul ar trebui să fie:

``` text
$ sudo nmap -p- -O 192.168.56.104
[sudo] password for kali: 
Sorry, try again.
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-08 08:51 EST
Nmap scan report for 192.168.56.104
Host is up (0.00096s latency).
Not shown: 65505 closed tcp ports (reset)
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
25/tcp    open  smtp
53/tcp    open  domain
80/tcp    open  http
111/tcp   open  rpcbind
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
512/tcp   open  exec
513/tcp   open  login
514/tcp   open  shell
1099/tcp  open  rmiregistry
1524/tcp  open  ingreslock
2049/tcp  open  nfs
2121/tcp  open  ccproxy-ftp
3306/tcp  open  mysql
3632/tcp  open  distccd
5432/tcp  open  postgresql
5900/tcp  open  vnc
6000/tcp  open  X11
6667/tcp  open  irc
6697/tcp  open  ircs-u
8009/tcp  open  ajp13
8180/tcp  open  unknown
8787/tcp  open  msgsrvr
34659/tcp open  unknown
38945/tcp open  unknown
40256/tcp open  unknown
52250/tcp open  unknown
MAC Address: 08:00:27:B9:20:DA (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 3.76 seconds
```

## Exploitation

Înarmați cu informațiile obținute până acum, putem avansa către faza de exploatare a serviciilor vulnerabile.

Exploatați cât mai multe servicii expuse de mașina virtuală țintă.

În primul rând inspectați versiunea fiecărui serviciu expus.
Căutați online potențiale exploit-uri pentru versiunile în cauză.
Apoi folosiți `metasploit` pentru a exploata serviciile.
