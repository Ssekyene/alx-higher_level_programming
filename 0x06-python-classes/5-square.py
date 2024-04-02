#!/usr/bin/python3
# 5-square.py by Hasaan Ahmad
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

        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square to a given value.

        :param value: The new size of the square.
        :type value: int
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """

        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        :rtype: int
        """

        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square of size `self.__size` using the '#' character.
        If `self.__size` is 0, it prints an empty line.

        :param self: The instance of the class.
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
