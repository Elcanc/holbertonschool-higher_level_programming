#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a/b
        print("{}".format(r))
    except ZeroDivisionError:
        return None
