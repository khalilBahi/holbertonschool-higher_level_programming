#!/usr/bin/python3

"""
module my list
"""


class MyList(list):
    """create a list"""

    def print_sorted(self):
        """sort the list and print it"""
        my_list = sorted(self)
        print(my_list)
