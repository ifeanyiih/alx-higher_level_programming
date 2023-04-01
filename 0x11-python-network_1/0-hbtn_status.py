#!/usr/bin/python3
"""
This module contains a function which fetches data
from https://alx-intranet.hbtn.io/status and
displays the body of the response.

Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example
(tabulation before -)
You must use a with statement
"""

import urllib.request


def printBodyResponse(url):
    """Print the body of a url response

    Args:
        url (str): The url to fetch from
    """
    with urllib.request.urlopen(url) as response:
        output = f"""Body response:
    - type: {type(response.read())}
    - content: {response.read()}
    - utf8 content: {response.read().decode('utf-8')}"""
        print(output)


if __name__ == "__main__":
    printBodyResponse('https://alx-intranet.hbtn.io/status')
