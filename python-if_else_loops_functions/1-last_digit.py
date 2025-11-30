#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 == 0:
    msg = "is zero"
elif number % 10 < 6:
    msg = "is less than 6 and not zero"
else:
    msg = "is greater than 5"

print(f"The last digit of {number} is {number % 10} " \
        "and {msg}")
