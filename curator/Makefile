# SystemArguments
NAME = elasticsearch-curator
VERSION = 4.1

# Build Arguments
#HTTP_PROXY=
#HTTPS_PROXY=
#NO_PROXY=
BUILDARGS := $(shell cat buildargs.txt)

.PHONY: all build

build:
	docker build -t ${NAME}:${VERSION} .

tag_latest:
	docker tag ${NAME}:${VERSION} ${NAME}:latest
