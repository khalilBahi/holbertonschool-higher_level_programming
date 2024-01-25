#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    num = -(abs(number) % 10)
else:
    num = abs(number) % 10
if ((num < 0) or (6 > num > 0)):
    print("Last digit of", number, "is", num, "and is less than 6 and not 0")
elif (num == 0):
    print("Last digit of", number, "is", num, "and is 0")
else:
    print("Last digit of", number, "is", num, "and is greater than 5")
