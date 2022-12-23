#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    arr = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, IndexError, ZeroDivisionError) as e:
            if type(e) == TypeError:
                print("wrong type")
            if type(e) == IndexError:
                print("out of range")
            if type(e) == ZeroDivisionError:
                print("division by 0")
        finally:
            arr.append(result)
            result = 0
    return arr
