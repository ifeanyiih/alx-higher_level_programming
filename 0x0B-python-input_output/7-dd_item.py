#!/usr/bin/python3

"""
Module adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

if len(sys.argv) == 1:
    save_to_json_file([], file_name)
else:
    items = sys.argv[1:]
    load_file = load_from_json_file(file_name)
    for item in items:
        load_file.append(item)
    save_to_json_file(load_file, file_name)
