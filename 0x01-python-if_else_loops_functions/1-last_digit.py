#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10) is 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
else:
    l = (number % 10) if number > 0 else -((-number) % 10)
    if l > 5:
        print("Last digit of", number, "is", l, "and is greater than 5")
    else:
        print("Last digit of", number, "is", l, "and is less than 6 and not 0")
