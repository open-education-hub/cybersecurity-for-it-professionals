all: arbitrary-write

arbitrary-write: arbitrary-write.c
	gcc -m32 -zexecstack -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-PIC -o $@ $<

clean:
	rm -f arbitrary-write
