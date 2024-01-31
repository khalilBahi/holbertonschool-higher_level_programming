#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for i in my_list:
        if i == search:
            i = replace
        result.append(i)
    return result
