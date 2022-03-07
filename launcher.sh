#!/bin/sh
image=$(docker image build --quiet .)
docker container run --interactive --tty --name="logger" --user="$(id --user)" --volume="$PWD"/output:/logger/output --rm "$image"