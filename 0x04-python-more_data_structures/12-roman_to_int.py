#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return (0)
    roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            }
    roman_total = 0
    next_value = 0

    for charc in reversed(roman_string):
        if charc in roman_num:
            immediate_val = roman_num[charc]
        else:
            immediate_val = 0
        if immediate_val < next_value:
            roman_total = roman_total - immediate_val
        else:
            roman_total = roman_total + immediate_val
        next_value = immediate_val
    return (roman_total)
