#!/usr/bin/python3
def best_score(a_dictionary):
    list = []
    for i in a_dictionary:
        if isinstance(a_dictionary[i], int):
            list.append(a_dictionary[i])
    new = sorted(list)
    return new[-1]
