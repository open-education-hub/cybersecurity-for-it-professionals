all: shellcode-static

shellcode-static: shellcode-static.c
	gcc -m32 -zexecstack -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-PIC -o $@ $<

clean:
	rm -f shellcode-static
