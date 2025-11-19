#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list):
        return None
    elif idx < 0:
        return None
    else:
        a = my_list[idx]
        print("Element at index {:d} is {}".format(idx, a))
