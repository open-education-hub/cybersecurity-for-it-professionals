# build: docker build -t csitp-03_sgid-thing .
# run: docker run -dit --name csitp-03_sgid-thing -p 30103:22 csitp-03_sgid-thing
# stop: docker stop csitp-03_sgid-thing
FROM debian:11

RUN apt-get -y update; apt-get -y install ssh vim nano sudo; apt-get -y update --fix-missing

COPY flag setup /
RUN /setup; rm /flag /setup

ENTRYPOINT service ssh restart && /bin/bash
