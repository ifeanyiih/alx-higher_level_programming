#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except Exception:
        pass
    finally:
        if result == 0:
            result = None
        print("Inside result: {}".format(result))

