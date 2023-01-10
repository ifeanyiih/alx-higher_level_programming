#!/usr/bin/python3

"""
Module adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

if not path.exists(file_name):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write('[]')
obj = load_from_json_file(file_name)
for item in sys.argv[1:]:
    obj.append(item)
save_to_json_file(obj, file_name)
