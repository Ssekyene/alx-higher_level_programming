#!/bin/bash
# URL sends GET request to  URL & displays the body of the response 200. Try ./1-body.sh 0.0.0.0:80/[path]
curl -sL "$1"
