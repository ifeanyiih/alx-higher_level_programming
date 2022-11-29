#!/usr/bin/python3
import random
from sys import stderr
number = random.randint(-10000, 10000)
stderr.write(f"Last digit of {number:d} is {number%10:d}")
if number % 10 == 0:
    stderr.write(f" and is 0\n")
elif number % 10 < 6:
    stderr.write(f" and is less than 6 and not 0\n")
elif number % 10 > 5:
    stderr.write(f" and is greater than 5\n")
