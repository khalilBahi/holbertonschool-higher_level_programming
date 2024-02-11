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
