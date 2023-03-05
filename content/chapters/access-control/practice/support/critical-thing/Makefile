build:
	docker build -t csitp-03_critical-thing .

export: build
	docker save -o csitp-03_critical-thing.tar csitp-03_critical-thing

run: build
	docker run -dit --name csitp-03_critical-thing -p 30102:22 csitp-03_critical-thing

stop:
	docker stop csitp-03_critical-thing

clean: stop
	docker rm csitp-03_critical-thing
	docker image rm csitp-03_critical-thing
