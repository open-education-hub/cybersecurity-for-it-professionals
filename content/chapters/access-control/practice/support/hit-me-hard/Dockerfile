FROM ubuntu:20.04

RUN apt-get -y update; apt-get -y install ssh; apt-get install -y libcap2 libcap2-bin; apt-get -y update --fix-missing

RUN useradd -m -d /home/ctf -s /bin/bash ctf \
    && passwd -l ctf > /dev/null \
    && passwd -n 9999 ctf > /dev/null \
    && chown -R root:ctf /home/ctf \
    && chmod 750 /home/ctf
RUN echo "ctf:hit-me-hard-0" | chpasswd && passwd -u ctf > /dev/null

COPY secret /home/ctf/secret
RUN chown root:ctf /home/ctf/secret \
    && chmod 400 /home/ctf/secret \
    && setcap cap_dac_read_search+ep /usr/bin/rev \
    && chmod o+x /sbin/getcap

ENTRYPOINT service ssh restart && /bin/bash
