all: buffer-management-segfault

buffer-management-segfault: buffer-management-segfault.c
	gcc -m32 -zexecstack -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-PIC -o $@ $<

clean:
	rm -f buffer-management-segfault
