#!/usr/bin/python3

def safe_print_integer_err(value):
    rslt = True
    try:
        print("{:d}".format(value))
    except:
        rslt = False
    finally:
        return rslt
