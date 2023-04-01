#!/bin/bash
#  a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [[ $(curl -o text -w "%{http_code}" "$1") == "200" ]];then cat text; rm text; fi; rm text
