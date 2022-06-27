#!/bin/sh
# Used to set the user and group ID in order to run the container with execution
# rights equals to the one used in the session creating the container
export DOCKER_UID=$(id -u)
export DOCKER_GID=$(id -g)
docker-compose up -d
