#!/bin/bash
curl -sI "$1" | grep "HTTP*"| cut -d " " -f 2| cat
