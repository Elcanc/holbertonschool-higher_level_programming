#!/usr/bin/python3
def best_score(a_dictionary):
    list = []
    for i in a_dictionary:
        if isinstance(a_dictionary[i], int):
            list.append(a_dictionary[i])
    new = sorted(list)
    a = new[-1]
    for key, value in a_dictionary.items():
        if value == a:
            best_key = key
    return best_key
