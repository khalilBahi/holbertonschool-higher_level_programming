#!/usr/bin/python3

"""
This module provides a function to look up
attributes and methods of an object.
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False."""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
