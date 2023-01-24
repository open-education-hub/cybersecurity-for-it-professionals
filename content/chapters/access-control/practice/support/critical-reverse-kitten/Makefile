build:
	docker build -t csitp-03_critical-reverse-kitten .

export: build
	docker save -o csitp-03_critical-reverse-kitten.tar csitp-03_critical-reverse-kitten

run: build
	docker run -dit --name csitp-03_critical-reverse-kitten -p 30102:22 csitp-03_critical-reverse-kitten

stop:
	docker stop csitp-03_critical-reverse-kitten

clean: stop
	docker rm csitp-03_critical-reverse-kitten
	docker image rm csitp-03_critical-reverse-kitten
