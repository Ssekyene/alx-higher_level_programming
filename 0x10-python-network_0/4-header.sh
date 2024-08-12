#!/bin/bash
# URL arg, sends GET request to URL, and display  body of the response. eg ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
curl -s "$1" -X GET -H "X-School-User-Id: 98"
