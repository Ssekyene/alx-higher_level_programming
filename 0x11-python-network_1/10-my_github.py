#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
The first argument will be your username
The second argument will be your password (in your case,
a personal access token as password)
Example usage: ./10-my_github.py papamuziko cisfun
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    passwd = argv[2]
    res = requests.get(url, auth=HTTPBasicAuth(user, passwd))
    print(res.json().get('id'))
