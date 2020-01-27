#!/usr/bin/python3
''' Module that has the Class of Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Class that represents a square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor method
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' Get property for size
        '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Set property for size
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' Updats the information of the objejct
        '''
        att = ("id", "size", "x", "y")
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        ''' Returns a dictionary representation of the object'''
        att = ("id", "size", "size", "x", "y")
        dic = dict()
        for a in att:
            dic[a] = getattr(self, a)
        return dic

    def __str__(self):
        ''' Overload method for __str__
        '''
        r_str = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return r_str.format(self.id, self.x, self.y, self.width)
