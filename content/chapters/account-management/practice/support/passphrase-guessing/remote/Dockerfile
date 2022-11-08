# build: docker build -t citp-02_passphrase-guessing .
# run: docker run -dit --name citp-02_passphrase-guessing -p 20101:1337 citp-02_passphrase-guessing
# stop: docker stop citp-02_passphrase-guessing
FROM ubuntu:20.04

RUN apt-get -y update; apt-get -y install python3 xinetd
RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN passwd -l ctf
RUN passwd -n 9999 ctf
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN echo "ctf:somepassword" | chpasswd
RUN passwd -u ctf
RUN mkdir /home/ctf/passphrase-guessing

COPY secret passphrase-guessing.py adjectives.txt articles.txt nouns.txt /home/ctf/passphrase-guessing/
COPY xinetd.conf /etc/xinetd.d/passphrase-guessing

ENTRYPOINT service xinetd start && /bin/bash
