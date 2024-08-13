# 0x11. Python - Network #1

## Concepts
* Python
* Scripting
* Back-end
* API

## Learning Objectives
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Code Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file at the root of the repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* You must use [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* Your code should not be executed when imported (by using if __name__ == "__main__":)

**FYI:**

- Files with prefixes from 0- to 3- use the `urllib` package while the proceeding files use the `requests` package which is the simpler one.
- The file [10-my_github.py](./10-my_github.py) uses [Basic Authentication](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28)  with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to access to the github user information (only `read:user` permission is needed)
- The file [recompile_python.sh](./recompile_python.sh) may be used to help in solving incompatibility issues of `requests` package with openssl.
- **Be careful: only 60 requests by hour by IP for unauthenticated requests [Rate limit](https://docs.github.com/en/rest)** 

## References
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

