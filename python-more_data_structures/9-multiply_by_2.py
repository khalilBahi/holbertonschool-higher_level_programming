#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = {}
    b_dic.update((key, value * 2) for key, value in a_dictionary.items())
    return b_dic
