#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' Return the current square size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets a new valur for the size of the square
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Returns the position of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0 or \
           type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' Return the current square area
        '''
        return self.__size ** 2

    def my_print(self):
        ''' Prints in stdout the square with the char #
        '''
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print("{:s}{:s}".format(' ' * self.__position[0],
                                    '#' * self.__size))
