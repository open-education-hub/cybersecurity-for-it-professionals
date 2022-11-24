# build: docker build -t sis-04_silent-speaker .
# run: docker run -dit --name sis-04_silent-speaker -p 40001:80 sis-04_silent-speaker
# stop: docker stop sis-04_silent-speaker
FROM debian:11

RUN apt-get -y update; apt-get -y install apache2 php libapache2-mod-php
COPY flag /
COPY index.php /var/www/html/
RUN chmod a+r /flag

ENTRYPOINT service apache2 restart && /bin/bash 
