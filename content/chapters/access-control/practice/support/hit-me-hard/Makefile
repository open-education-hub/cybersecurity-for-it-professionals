build:
	docker build -t csitp-03_hit-me-hard .

export: build
	docker save -o csitp-03_hit-me-hard.tar csitp-03_hit-me-hard

run: build
	docker run -dit --cap-add=cap_dac_read_search --name csitp-03_hit-me-hard -p 30102:22 csitp-03_hit-me-hard

stop:
	docker stop csitp-03_hit-me-hard

clean: stop
	docker rm csitp-03_hit-me-hard
	docker image rm csitp-03_hit-me-hard
