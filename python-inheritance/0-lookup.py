#!/usr/bin/python3

"""
This module provides a function to look up
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns:
        Returns list of object's attributes/methods
    """
    return dir(obj)
