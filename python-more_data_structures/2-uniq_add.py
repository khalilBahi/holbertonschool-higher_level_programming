#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set(my_list)
    s = 0
    for i in result:
        s += i
    return s
