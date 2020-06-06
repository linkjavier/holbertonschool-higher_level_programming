#!/usr/bin/python3
"""
    Function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
        Function that creates an Object from a “JSON file”
    """
    with open(filename) as my_file:
        return (json.loads(my_file.read()))
