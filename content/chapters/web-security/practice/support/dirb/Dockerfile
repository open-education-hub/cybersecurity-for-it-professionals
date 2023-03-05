# build: docker build -t sis-04_dirb .
# run: docker run -dit --name sis-04_dirb -p 40000:80 sis-04_dirb
# stop: docker stop sis-04_dirb
FROM debian:11

RUN apt-get -y update; apt-get -y install apache2
COPY setup /tmp
RUN /tmp/setup; rm /tmp/setup

ENTRYPOINT service apache2 restart && /bin/bash 
