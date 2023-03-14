# Runtime Application Security: Quiz

## Memory write

Care dintre următoarele este o formă de arbitrary memory write?

- information leak
- buffer overflow
- control flow integrity
- static analysis

## Static analysis

Care dintre următoarele este un utilitar de analiză statică?

- GDB (GNU Debugger)
- strace
- IDA (Interactive Disassembler)
- lsof

## Shellcode

Care dintre următoarele corelează cel mai bine cu shellcode?

- code reuse
- code pointer
- code injection
- stack canary

## Defensive mechanisms

Care dintre următoarele NU este un mecanism defensiv la nivelul memoriei?

- data execution prevention
- stack canary
- arbitrary memory read
- address space layout randomization

## Buffer overflow

Care dintre următoarele este un buffer overflow?

- int_16 n; int_64 m; m = n;
- char buf[10]; fgets(buf, 30, stdin);
- printf("%d\n", 1000);
- if (uid == 0) run_as_root();
