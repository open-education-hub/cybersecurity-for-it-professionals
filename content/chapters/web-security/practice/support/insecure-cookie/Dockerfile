# build: docker build -t csitp-06_insecure-cookie .
# run: docker run -dit --name csitp-06_insecure-cookie -p 40101:5000 csitp-06_insecure-cookie
# stop: docker stop csitp-06_insecure-cookie
# stop and remove: docker stop csitp-06_insecure-cookie && docker rm csitp-06_insecure-cookie && docker image rm csitp-06_insecure-cookie:latest
FROM debian:11

RUN apt-get -y update; apt-get -y install python3 python3-pip; pip3 install Flask
RUN mkdir /app
RUN mkdir /app/template
COPY app.py /app/
COPY index.html /app/templates/
WORKDIR /app

ENTRYPOINT FLASK_APP=app flask run --host=0.0.0.0 && /bin/bash 
