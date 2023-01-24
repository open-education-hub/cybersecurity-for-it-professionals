build:
	docker build -t csitp-03_reverse-kitten .

export: build
	docker save -o csitp-03_reverse-kitten.tar csitp-03_reverse-kitten

run: build
	docker run -dit --name csitp-03_reverse-kitten -p 30100:22 csitp-03_reverse-kitten

stop:
	docker stop csitp-03_reverse-kitten

clean: stop
	docker rm csitp-03_reverse-kitten
	docker image rm csitp-03_reverse-kitten
