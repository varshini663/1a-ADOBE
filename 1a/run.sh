#!/bin/bash

# Build the Docker image
docker build --platform linux/amd64 -t pdf-outline-extractor .

# Run the container
docker run --rm -v "$(pwd)/app/input:/app/input" -v "$(pwd)/app/output:/app/output" pdf-outline-extractor