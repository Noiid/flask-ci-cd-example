@echo off

docker build -t "blog-app-ci-cd" -f "Dockerfile" .

docker run -p 8080:8080 "blog-app-ci-cd"