#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': argv[2]})
    email = email.encode('ascii')
    req = urllib.request.Request(argv[1], email)
    try:
        with urllib.request.urlopen(req) as resp:
            if resp:
                html = resp.read()
                print(html.decode('utf-8'))
    except Exception:
        pass
