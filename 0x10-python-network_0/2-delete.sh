#!/bin/bash
# send DELETE request to URL passed as first arg & display body of response. eg ./2-delete.sh 0.0.0.0:5000/route_3 ; echo "" 
curl -sX DELETE "$1"
