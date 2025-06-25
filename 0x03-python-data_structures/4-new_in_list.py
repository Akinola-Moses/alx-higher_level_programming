#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_listcopy = my_list[:]
    if 0 > idx or idx >= len(my_list):
        return (my_listcopy)
    my_listcopy[idx] = element
    return (my_listcopy)
