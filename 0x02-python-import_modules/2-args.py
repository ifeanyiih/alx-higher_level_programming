#!/usr/bin/python3
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} ", end="")
        if len(sys.argv) - 1 > 1:
            print("arguments:")
        else:
            print("argument:")

        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
