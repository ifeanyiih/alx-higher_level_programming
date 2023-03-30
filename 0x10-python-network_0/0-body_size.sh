#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -I --no-progress-meter $1 | grep -oE "Content-Length: [0-9]+" | cut -d " " -f 2 | cat
