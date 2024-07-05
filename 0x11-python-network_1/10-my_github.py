#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    passw = argv[2]
    res = requests.get(url, auth=HTTPBasicAuth(user, passw))
    print(res.json().get('id'))
