#!/usr/bin/python3
"""Write a class Square that defines a square by size"""


class Square():
    """ create a square"""
    def __init__(self, size=0):
        """ inisalise the size of the square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
