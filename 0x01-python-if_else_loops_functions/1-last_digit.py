#!/usr/bin/python3
import random, sys
number = random.randint(-10000, 10000)
sys.stderr.write(f"Last digit of {number:d} is {number%10:d}")
if number % 10 == 0:
    sys.stderr.write(f" and is 0\n")
elif number % 10 < 6:
    sys.stderr.write(f" and is less than 6 and not 0\n")
elif number % 10 > 5:
    sys.stderr.write(f" and is greater than 5\n")
