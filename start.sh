#!/usr/bin/env bash

if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker to proceed."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose to proceed."
    exit 1
fi

sudo docker-compose down

sudo docker-compose up --build --remove-orphans -d

sudo docker-compose ps

sudo docker-compose logs
