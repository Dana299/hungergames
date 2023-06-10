SHELL := /bin/bash

run:
	source run_all.sh

stop:
	@echo "___Stopping httpbin container___"
	docker stop $(shell docker ps -q --filter ancestor=kennethreitz/httpbin)

clean:
	@echo "___Removing httpbin container___"
	docker rm $(shell docker ps -aq --filter ancestor=kennethreitz/httpbin)