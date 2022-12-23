#!/usr/bin/python3

import sys


def safe_print_integer_err(value):

    rslt = True
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write('Exception: ' + str(e) + '\n')
    return False
