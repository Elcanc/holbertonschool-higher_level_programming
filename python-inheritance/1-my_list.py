#!/usr/bin/python3
"""#"""


class MyList(list):
    """Inherits from list and adds a method to print the list sorted"""

    def print_sorted(self):
        """ Inherits from list and adds a method to print sorted list. """

        print(sorted(self))
