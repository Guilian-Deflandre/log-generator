#!/bin/sh
image=$(docker image build --quiet .)
docker container run --interactive --tty --name="logger" --user="$(id -u)" --volume="$PWD"/output:/logger/output --rm "$image"