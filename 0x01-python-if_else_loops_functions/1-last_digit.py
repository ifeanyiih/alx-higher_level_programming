#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10
print(f"Last digit of {number} is {rem}", end=" ")
if rem == 0:
    print(f"and is 0")
elif rem < 6:
    print(f"and is less than 6 and not 0")
else:
    print(f"and is greater than 5")
