#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            if resp:
                html = resp.read()
                print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
