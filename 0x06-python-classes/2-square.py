#!/usr/bin/python3
# 2-square.py by Robert Ssekyene
"""defines a square"""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        :param size: The size of the square. Default value is 0.
        :type size: int
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
