#!/bin/bash
# sends request to URL passed as arg & displays status code of the response. eg ./100-status_code.sh 0.0.0.0:5000 ; echo ""
curl -o /dev/null -w '%{http_code}' -sLI "$1"
