#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        ''' Return the current square size
        '''
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' Return the current square area
        '''
        return self.__size ** 2

    def __lt__(self, other):
        return True if self.__size < other.size else False

    def __le__(self, other):
        return True if self.__size <= other.size else False

    def __eq__(self, other):
        return True if self.__size == other.size else False

    def __ne__(self, other):
        return True if self.__size != other.size else False

    def __ge__(self, other):
        return True if self.__size >= other.size else False

    def __gt__(self, other):
        return True if self.__size > other.size else False
