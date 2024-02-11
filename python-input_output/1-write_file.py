#!/usr/bin/python3
""" python input output """


def write_file(filename="", text=""):
    """write file"""
    with open(filename, "w") as f:
        return f.write(text)
