#!/usr/bin/python3
"""Technical interview preparation:
You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.
Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need
to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n),
O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """Finds the peak value, in a list of integers

    Args:
        list_of_integers (list): list_of_integers
    Returns:
        peak (int): the peak value
    """
    peak = None
    if len(list_of_integers) == 0:
        return peak
    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] > list_of_integers[i + 1]:
                peak = list_of_integers[i]
                return peak
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                peak = list_of_integers[i]
                return peak
        else:
            if (list_of_integers[i] > list_of_integers[i + 1]) and\
            (list_of_integers[i] > list_of_integers[i - 1]):
                peak = list_of_integers[i]
                return peak
