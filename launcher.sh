#!/bin/sh
#image=$(docker image build --quiet .)
#docker container run --detach --name="logger" --user="$(id -u)" --volume="$PWD"/output:/logger/output --rm "$image" 
export UID=${UID}
export GID=${GID}
docker-compose up -d
