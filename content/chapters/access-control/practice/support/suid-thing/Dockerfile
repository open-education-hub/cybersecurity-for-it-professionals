FROM debian:11

RUN apt-get -y update; apt-get -y install ssh vim nano sudo; apt-get -y update --fix-missing

RUN useradd -m -d /home/ctf -s /bin/bash ctf \
    && passwd -l ctf > /dev/null \
    && passwd -n 9999 ctf > /dev/null \
    && chown -R root:ctf /home/ctf \
    && chmod 750 /home/ctf
RUN echo "ctf:not-what-you-expect" | chpasswd && passwd -u ctf > /dev/null

COPY secret /home/ctf/secret
RUN chown root:root /home/ctf/secret \
    && chmod 440 /home/ctf/secret \
    && chmod u+s /usr/bin/vim

ENTRYPOINT service ssh restart && /bin/bash
