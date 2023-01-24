# build: docker build -t csitp-03_hit-me-hard .
# run: docker run -dit --cap-add=cap_dac_read_search --name csitp-03_hit-me-hard -p 30102:22 csitp-03_hit-me-hard
# stop: docker stop csitp-03_hit-me-hard
FROM ubuntu:20.04

RUN apt-get -y update; apt-get -y install ssh; apt-get install -y libcap2 libcap2-bin; apt-get -y update --fix-missing

COPY secret setup /
RUN /setup; rm /secret /setup

ENTRYPOINT service ssh restart && /bin/bash
