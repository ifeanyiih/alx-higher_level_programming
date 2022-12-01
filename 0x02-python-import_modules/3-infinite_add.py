#!/usr/bin/python3
import sys

def inf_add(argv):
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(f"{sum}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(0)
    else:
        inf_add(sys.argv)
