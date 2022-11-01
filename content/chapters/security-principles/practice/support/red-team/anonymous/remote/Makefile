run:
		docker build -t citp-01_anonymous .
		docker run -dit --name citp-01_anonymous -p 10022:22 -p 10021:21 -p 65400-65500:65400-65500 citp-01_anonymous

stop:
		docker stop citp-01_anonymous
