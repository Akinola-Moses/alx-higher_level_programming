#!/usr/bin/python3
def remove_char_at(str, n):
    s_cpy = ''
    idx = 0
    while (idx < len(str)):
        if (idx != n):
            s_cpy += str[idx]
        idx = idx + 1
    return (s_cpy)
