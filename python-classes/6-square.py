#!/usr/bin/python3
"""Write a class Square that defines a square by size
    and calculate current square area """


class Square:
    """create a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.__size = size

    @property
    def size(self):
        """getter for the size"""
        return self.__size

    @property
    def position(self):
        """getter for the position"""
        return self.__position

    @size.setter
    def size(self, size):
        """setter for the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        """setter for the position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """function that returns the current square area"""
        return self.__size**2

    def my_print(self):
        """function that print the square with # in a spesial position"""
        if self.__size == 0:
            print()
        else:
            print("{}".format("\n" * self.__position[1]), end="")
            for i in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size))
