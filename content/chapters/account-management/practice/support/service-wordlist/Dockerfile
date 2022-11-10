# build: docker build -t citp-02_service-wordlist .
# run: docker run -dit --name citp-02_service-wordlist -p 20003:22 citp-02_service-wordlist
# stop: docker stop citp-02_service-wordlist
FROM debian:11

RUN apt-get -y update; apt-get -y install ssh; apt-get -y update --fix-missing

COPY secret setup /
RUN /setup; rm /secret /setup

ENTRYPOINT service ssh restart && /bin/bash
