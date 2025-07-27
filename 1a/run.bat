@echo off
REM Build the Docker image
docker build --platform linux/amd64 -t pdf-outline-extractor .

REM Run the container
docker run --rm -v "%CD%\app\input:/app/input" -v "%CD%\app\output:/app/output" pdf-outline-extractor