# build: docker build -t csitp-03_reverse-kitten .
# run: docker run -dit --name csitp-03_reverse-kitten -p 30100:22 csitp-03_reverse-kitten
# stop: docker stop csitp-03_reverse-kitten
FROM debian:11

RUN apt-get -y update; apt-get -y install ssh vim nano sudo; apt-get -y update --fix-missing

COPY secret setup /
RUN /setup; rm /secret /setup

ENTRYPOINT service ssh restart && /bin/bash
