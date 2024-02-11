#!/usr/bin/python3
""" python input output """


def append_write(filename="", text=""):
    """function that appends a string at the end of
    a text file and returns the number of charachters added"""
    with open(filename, "a") as f:
        return f.write(text)
