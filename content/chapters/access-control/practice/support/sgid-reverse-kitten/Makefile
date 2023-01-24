build:
	docker build -t csitp-03_sgid-reverse-kitten .

export: build
	docker save -o csitp-03_sgid-reverse-kitten.tar csitp-03_sgid-reverse-kitten

run: build
	docker run -dit --name csitp-03_sgid-reverse-kitten -p 30101:22 csitp-03_sgid-reverse-kitten

stop:
	docker stop csitp-03_sgid-reverse-kitten

clean: stop
	docker rm csitp-03_sgid-reverse-kitten
	docker image rm csitp-03_sgid-reverse-kitten
