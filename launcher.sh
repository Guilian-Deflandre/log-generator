#!/bin/sh
export DOCKER_UID=$(id -u)
export DOCKER_GID=$(id -g)
docker-compose up -d
