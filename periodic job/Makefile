VERSION=v4

build:
	docker build -t periodic .

push:
	docker tag periodic gcr.io/datacenter-csci-5253/periodic
	docker push gcr.io/datacenter-csci-5253/periodic