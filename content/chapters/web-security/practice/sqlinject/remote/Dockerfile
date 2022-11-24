# build: docker build -t sis-04_sqlinject .
# run: docker run -dit --name sis-04_sqlinject -p 40003:80 sis-04_sqlinject
# stop: docker stop sis-04_sqlinject
FROM debian:11

RUN apt-get -y update; apt-get -y install apache2 php7.4 libapache2-mod-php7.4 php-mysql
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mariadb-server-10.3 mysql-server/root_password password somenastyrootpass'"]
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mariadb-server-10.3 mysql-server/root_password_again password somenastyrootpass'"]
RUN apt-get -y install mariadb-server
COPY flag index.php login.php sql /var/www/html/
#RUN chmod a+r /var/www/html/flag

ENTRYPOINT service apache2 restart && service mariadb start && (cat /var/www/html/sql | mysql -h localhost -u root -psomenastyrootpass) && /bin/bash 
