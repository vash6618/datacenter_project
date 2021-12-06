VERSION=v4

build:
	docker build -t database .

push:
	docker tag database gcr.io/datacenter-csci-5253/database
	docker push gcr.io/datacenter-csci-5253/database