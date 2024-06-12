#!/bin/bash

docker build -t 'blog-app-ci-cd' -f 'Dockerfile.local' .

docker run -p 8080:8080 'blog-app-ci-cd'

