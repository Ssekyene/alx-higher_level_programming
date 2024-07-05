#!/usr/bin/python3
"""
script that takes in a URL & email, sends a POST request to the passed URL
with email as param & displays the body of response (decoded in utf-8)
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    params = {'email': argv[2]}
    response = requests.post(url, params)
    print(response.text)
