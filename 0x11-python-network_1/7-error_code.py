#!/usr/bin/python3
"""
script takes in URL, sends request to URL & displays body
of response (decoded in utf-8)
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
