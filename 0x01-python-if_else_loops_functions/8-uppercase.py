#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        code = ord(str[i])
        if code >= 97 and code <= 122:
            code -= 32
        print("{}".format(chr(code)), end="")
    print()
