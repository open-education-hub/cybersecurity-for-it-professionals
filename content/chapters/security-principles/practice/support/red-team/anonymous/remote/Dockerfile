FROM ubuntu:20.04

RUN apt-get -y update; apt-get -y install ssh vsftpd; apt-get -y update --fix-missing

COPY secret setup /
RUN /setup; rm /secret /setup

ENTRYPOINT service ssh restart && service vsftpd restart && /bin/bash
