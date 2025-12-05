#!/usr/bin/python3
"""Returns True if obj is instance of a class that inherited from a_class"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is instance of a class
     that inherited from a_class
     """
    return isinstance(obj, a_class) and type(obj) is not a_class
    