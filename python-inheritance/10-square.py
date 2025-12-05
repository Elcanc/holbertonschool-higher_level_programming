#!/usr/bin/python3
"""square"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
