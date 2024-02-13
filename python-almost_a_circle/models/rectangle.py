#!/usr/bin/python3
"""
module Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object with the specified
        width, height, x, y, and optional id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width=value
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height=value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x=value
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y=value