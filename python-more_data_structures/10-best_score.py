#!/usr/bin/python3
def best_score(a_dictionary):
    list = []
    if not a_dictionary:
        return None
    for i in range(len(a_dictionary)):
        list.append(a_dictionary[i])
    new = sorted(list)
    return new[-1]
