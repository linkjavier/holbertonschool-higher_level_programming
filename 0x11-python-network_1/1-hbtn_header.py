#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            if resp:
                xreq_id = resp.getheader('X-Request-Id')
            print(xreq_id)
    except Exception:
        pass
