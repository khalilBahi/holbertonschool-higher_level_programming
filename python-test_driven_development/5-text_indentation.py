#!/usr/bin/python3
"""
Function to add indentation to text based on certain punctuation marks
"""


def text_indentation(text):
    """
    Format the input text by adding 2 newlines after (:?.)
        Args:
            text (str): The input text to be formatted.
        Raises:
            TypeError: If the 'text' argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    dlm = ['.', '?', ':']
    modified_text = ""

    line = ""
    for ch in text:
        if ch in dlm and line:
            modified_text += line.rstrip() + ch + " \n\n"
            line = ""
        else:
            line += ch

    if line:
        modified_text += line.rstrip() + "\n"

    print(modified_text, end="")
    