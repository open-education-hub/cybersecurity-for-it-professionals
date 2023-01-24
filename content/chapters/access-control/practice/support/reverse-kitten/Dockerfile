FROM debian:11

RUN apt-get -y update; apt-get -y install ssh vim nano sudo; apt-get -y update --fix-missing

RUN useradd -m -d /home/ctf -s /bin/bash ctf \
    && passwd -l ctf > /dev/null \
    && passwd -n 9999 ctf > /dev/null \
    && chown -R root:ctf /home/ctf \
    && chmod 750 /home/ctf
RUN echo "ctf:reverse-kitten-0" | chpasswd && passwd -u ctf > /dev/null

COPY secret /home/ctf/secret
RUN chown root:ctf /home/ctf/secret \
    && chmod 400 /home/ctf/secret \
    && echo "ctf ALL=NOPASSWD:/usr/bin/tac secret" | (su -c 'EDITOR="tee" visudo -f /etc/sudoers.d/tac > /dev/null')

ENTRYPOINT service ssh restart && /bin/bash
