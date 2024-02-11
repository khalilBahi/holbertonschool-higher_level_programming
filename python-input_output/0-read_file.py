#!/usr/bin/python3
""" python input output """


def read_file(filename=""):
    """reading file"""
    with open(filename, encoding="utf-8") as f:
        for ch in f:
            print(ch, end="")
