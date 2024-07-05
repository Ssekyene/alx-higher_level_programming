#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    res = requests.post(url, data=data)

    try:
        data_dict = res.json()
        if data_dict:
            print("[{}] {}".format(data_dict.get('id'), data_dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
