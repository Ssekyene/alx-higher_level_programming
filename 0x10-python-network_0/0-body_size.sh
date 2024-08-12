#!/bin/bash
# Sends request to URL, & display size of the body of the response. try ./0-body_size.sh 0.0.0.0:80
curl -sI "$1" | grep "Content-Length:" | cut -f2 -d' '
