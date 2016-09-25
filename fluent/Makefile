# SystemArguments
NAME = fluent-es
VERSION = latest

# Build Arguments
#HTTP_PROXY=
#HTTPS_PROXY=
#NO_PROXY=
BUILDARGS := $(shell cat buildargs.txt)

.PHONY: all build

build:
	docker build -t ${NAME}:${VERSION} .
