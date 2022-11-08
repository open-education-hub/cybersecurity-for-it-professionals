# build: docker build -t citp-02_sidechannel .
# run: docker run -dit --name citp-02_sidechannel -p 20102:1337 citp-02_sidechannel
# stop: docker stop citp-02_sidechannel
FROM ubuntu:20.04

RUN apt-get -y update; apt-get -y install python3 xinetd
RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN passwd -l ctf
RUN passwd -n 9999 ctf
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN echo "ctf:somepassword" | chpasswd
RUN passwd -u ctf
RUN mkdir /home/ctf/sidechannel

COPY secret sidechannel.py /home/ctf/sidechannel/
COPY xinetd.conf /etc/xinetd.d/sidechannel

ENTRYPOINT service xinetd start && /bin/bash
