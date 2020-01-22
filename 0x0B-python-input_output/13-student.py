#!/usr/bin/python3
class Student:

    def __init__(self, firt_name, last_name, age):
        self.first_name = firt_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__
        else:
            return dict(filter(lambda x: x[0] in attrs, self.__dict__.items()))

    def reload_from_json(self, json):
        for key, val in json.items():
            if hasattr(self, key):
                setattr(self, key, val)
