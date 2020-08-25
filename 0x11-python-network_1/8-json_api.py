#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        letter = argv[1]
    except:
        letter = ""
    try:
        resp = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
        try:
            json_resp = resp.json()
            if len(json_resp) > 0:
                print("[{}] {}".format(json_resp['id'], json_resp['name']))
            elif len(json_resp) == 0:
                print("No result")
        except:
            print("Not a valid JSON")
    except:
        print("No result")
