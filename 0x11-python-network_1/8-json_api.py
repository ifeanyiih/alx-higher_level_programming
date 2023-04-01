#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        json = req.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")

    if int(req.status_code) == 204:
        print("No result")
    else:
        print(f"[{json[0]["id"]}] {json[0]["name"]}")
