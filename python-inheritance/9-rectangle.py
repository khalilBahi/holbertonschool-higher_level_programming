#!/usr/bin/python3

"""
module base geometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
