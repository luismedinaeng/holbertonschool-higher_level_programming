#!/usr/bin/python3
''' Module that has the class of Rectangle
'''
from models.base import Base


class Rectangle(Base):
    ''' Class that represents a rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor method
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' Get property for width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Set property for width
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' Get property for height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Set property for height
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' Get property for x coordinate
        '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' Set property for x coordinate
        '''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' Get property for y coordinate
        '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' Set property for y coordinate
        '''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Returns the area of a rectangle
        '''
        return self.__height * self.__width

    def display(self):
        ''' Prints the representation of the rectangle
        '''
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def update(self, *args, **kwargs):
        ''' Updates the information of the rectangle
        '''
        att = ("id", "width", "height", "x", "y")
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        ''' Returns a dictionary representation of the object
        '''
        att = ("id", "width", "height", "x", "y")
        dic = dict()
        i = 0
        for key, val in self.__dict__.items():
            if hasattr(self, att[i]):
                dic[att[i]] = val
            i += 1
        return dic

    def __str__(self):
        ''' Overload method of __str__
        '''
        r_str = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return r_str.format(self.id, self.__x, self.__y,
                            self.__width, self.__height)
