# build: docker build -t sis-05_web .
# run: docker run -dit --name sis-05_web -p 8003:80 sis-05_web
# stop: docker stop sis-05_web
FROM debian:11

RUN apt-get -y update; apt-get -y install apache2 php7.4 libapache2-mod-php7.4 php-mysql
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mariadb-server-10.3 mysql-server/root_password password somenastyrootpass'"]
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mariadb-server-10.3 mysql-server/root_password_again password somenastyrootpass'"]
RUN apt-get -y install mariadb-server
RUN chmod a+w /var/www/html
COPY flag-dummy index.php login.php logout.php sql /var/www/html/
COPY flag /

ENTRYPOINT service apache2 restart && service mariadb start && (cat /var/www/html/sql | mysql -h localhost -u root -psomenastyrootpass) && rm /var/www/html/sql && /bin/bash 
