#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -i -L -X OPTIONS $1 | grep "Allow: *"| cut -d " " -f1 --complement
