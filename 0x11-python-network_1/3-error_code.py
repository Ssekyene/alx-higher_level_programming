#!/usr/bin/python3
"""
script takes in URL, sends request to URL & displays body
of response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
