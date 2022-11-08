# build: docker build -t citp-02_sshguess .
# run: docker run -dit --name citp-02_sshguess -p 20003:22 citp-02_sshguess
# stop: docker stop citp-02_sshguess
FROM debian:11

RUN apt-get -y update; apt-get -y install ssh; apt-get -y update --fix-missing

COPY secret setup /
RUN /setup; rm /secret /setup

ENTRYPOINT service ssh restart && service vsftpd restart && /bin/bash
