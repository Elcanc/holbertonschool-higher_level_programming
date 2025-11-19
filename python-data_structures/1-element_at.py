#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx <0:
        return None
    return "Element at index {:d} is {}".format(idx, my_list[idx])
