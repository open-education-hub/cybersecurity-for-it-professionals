FROM debian:11

RUN apt-get -y update; apt-get -y install apache2 php libapache2-mod-php iputils-ping
COPY index.php /var/www/html/
COPY secret /
RUN chmod a+r /secret

ENTRYPOINT service apache2 restart && /bin/bash 
