#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or a_dictionary == {}):
        return None
    else:
        best_key = max(a_dictionary, key=a_dictionary.get)
    return (best_key)
