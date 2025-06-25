#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)
    max_num = my_list[0]
    for idx in my_list[1:]:
        if idx > max_num:
            max_num = idx
    return (max_num)
