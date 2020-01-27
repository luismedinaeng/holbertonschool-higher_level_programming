#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        str_save = []
        if list_objs != None:
            for obj in list_objs:
                str_save.append(obj.to_dictionary())
        str_save = cls.to_json_string(str_save)

        with open(cls.__name__ + ".json", mode="w") as a_file:
            a_file.write(str_save)
