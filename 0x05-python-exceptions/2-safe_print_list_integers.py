#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except Exception as e:
        raise e
    finally:
        print()
        return count
