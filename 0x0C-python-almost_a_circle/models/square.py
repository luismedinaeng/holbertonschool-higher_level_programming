#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        att = ("id", "size", "x", "y")
        if args != None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        att = ("id", "size", "size", "x", "y")
        dic = dict()
        i = 0
        for key, val in self.__dict__.items():
            if hasattr(self, att[i]):
                dic[att[i]] = val
            i += 1
        return dic

    def __str__(self):
        r_str = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return r_str.format(self.id, self.x, self.y, self.width)
