#!/usr/bin/python3
"""
    Function that returns an object (Python data structure)
    represented by a JSON string:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string:
    """
    with open(filename, "w") as j_file:
        j_file.write(json.dumps(my_obj))
