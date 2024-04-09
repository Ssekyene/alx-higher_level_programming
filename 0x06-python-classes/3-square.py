#!/usr/bin/python3
# 3-square.py by Robert Ssekyene
"""defines a square"""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        :param size: The size of the square. Default value is 0.
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        
        if type(size) != int or size < 0:
            if type(size) != int:
                raise TypeError('size must be an integer')
            else:
                raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        """

        return self.__size * self.__size
