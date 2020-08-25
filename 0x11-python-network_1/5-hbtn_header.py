#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp:
        print(resp.headers.get('X-Request-Id'))
