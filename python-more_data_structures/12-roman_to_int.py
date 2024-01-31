#!/usr/bin/python3
def roman_to_int(roman_string):
    rs = roman_string
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0
    if rs is None or not isinstance(rs, str):
        return 0

    while i < len(rs):
        if i + 1 < len(rs) and roman[rs[i]] < roman[rs[i + 1]]:
            result += roman[rs[i + 1]] - roman[rs[i]]
            i += 2
        else:
            result += roman[rs[i]]
            i += 1

    return result
