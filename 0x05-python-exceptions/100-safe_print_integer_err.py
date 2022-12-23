#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    rslt = True
    try:
        sys.stderr("{:d}".format(value))
    except Exception:
        rslt = False
    finally:
        return rslt
