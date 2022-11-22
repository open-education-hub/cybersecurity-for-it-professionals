all: buffer-management-notok

buffer-management-notok: buffer-management-notok.c
	gcc -m32 -zexecstack -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-PIC -o $@ $<

clean:
	rm -f buffer-management-notok
