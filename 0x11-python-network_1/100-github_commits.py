#!/usr/bin/python3
"""
list 10 commits DESC of the repository “rails” by the user “rails”
GitHub API doc: https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv


if __name__ == "__main__":

    repo_name = argv[1]
    owner_name = argv[2]
    url = f"https://api.github.com/repos/{owner_name}\
            /{repo_name}/commits/"

    res = requests.get(url)
    data = res.json()

    for i in range(0, 10):
        sha = data[i]['sha']
        author_name = data[i]['committer'].get('name')
        print(f"{sha}: {author_name}\n")
