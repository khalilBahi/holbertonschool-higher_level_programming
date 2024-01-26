#!/usr/bin/python3
def uppercase(str):
    upp = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upp += chr(ord(i) - 32)
        else:
            upp += i
    print("{}".format(upp))
