#!/usr/bin/python3
""" Python script that takes your Github credentials (username and password)
    and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    resp = requests.get('https://api.github.com/user', auth=(user, passwd))
    user = resp.json().get('id')
    print(user)
