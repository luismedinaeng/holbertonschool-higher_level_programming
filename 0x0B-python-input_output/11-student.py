#!/usr/bin/python3
class Student:

    def __init__(self, firt_name, last_name, age):
        self.first_name = firt_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
