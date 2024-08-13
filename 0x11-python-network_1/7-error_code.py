#!/usr/bin/python3
"""
script takes in URL, sends request to URL & displays body
of response (decoded in utf-8)
The script checks for the HTTP errors as well
Example usage: ./7-error_code.py http://0.0.0.0:5000
               ./7-error_code.py http://0.0.0.0:5000/status_401
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
