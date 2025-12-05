#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """Empty class"""
    pass

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if type(value) <= 0:
            raise ValueError(f"{name} must be greater than 0")
