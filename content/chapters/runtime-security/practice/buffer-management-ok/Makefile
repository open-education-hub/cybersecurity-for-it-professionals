all: buffer-management-ok

buffer-management-ok: buffer-management-ok.c
	gcc -m32 -zexecstack -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-PIC -o $@ $<

clean:
	rm -f buffer-management-ok
