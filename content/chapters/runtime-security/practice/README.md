# Runtime Application Security

Clonați [repository-ul](https://github.com/open-education-hub/cybersecurity-for-it-professionals), accesați branch-ul `raresvis-wip-runtime-application-security` și directorul `content/chapters/runtime-security/practice/`:

```
$ git clone https://github.com/open-education-hub/cybersecurity-for-it-professionals
$ cd cybersecurity-for-it-professionals/
$ git remote add raresvis https://github.com/raresvis/cybersecurity-for-it-professionals
$ git fetch raresvis
$ git checkout -b raresvis-wip-runtime-application-security raresvis/raresvis-wip-runtime-application-security
$ cd content/chapters/runtime-security/practice/
$ ls
arbitrary-read/   buffer-management-notok/  buffer-management-segfault/  python-memory-management/  shellcode-input/
arbitrary-write/  buffer-management-ok/     code-reuse/                  README.md                  shellcode-static/
```

Parcurgeți subdirectoarele în ordinea de mai jos.
Parcurgeți fișierul `README.md` și fișierele din fiecare subdirector.

1. [Buffer Management OK](./buffer-management-ok/)
1. [Buffer Management NOT OK](./buffer-management-notok/)
1. [Buffer Management SEGFAULT](./buffer-management-segfault/)
1. [Python Memory Management](./python-memory-management/)
1. [Arbitrary Read](./arbitrary-read/)
1. [Arbitrary Write](./arbitrary-write/)
1. [Shellcode Static](./shellcode-static/)
1. [Shellcode Input](./shellcode-input/)
1. [Code Reuse](./code-reuse/)
