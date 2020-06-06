#!/usr/bin/python3
"""
    Script that adds all arguments to a Python list,
    and then save them to a file
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    actual_cont = load_from_json_file(file_name)
except FileNotFoundError:
    actual_cont = []

save_to_json_file(actual_cont + argv[1:], file_name)
