build:
	docker build -t csitp-03_suid-thing .

export: build
	docker save -o csitp-03_suid-thing.tar csitp-03_suid-thing

run: build
	docker run -dit --name csitp-03_suid-thing -p 30101:22 csitp-03_suid-thing

stop:
	docker stop csitp-03_suid-thing

clean: stop
	docker rm csitp-03_suid-thing
	docker image rm csitp-03_suid-thing
