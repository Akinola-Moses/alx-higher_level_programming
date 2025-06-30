#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copyof_adic = {}
    for key in a_dictionary:
        copyof_adic[key] = a_dictionary[key] * 2
    return (copyof_adic)
