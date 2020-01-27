#!/usr/bin/python3
import json
'''Module that has the Base Class for figures
'''


class Base:
    '''Class that represents
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor method
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Convert a list of objects saved in dctionaries as json
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Save to a file a list of objects
        '''
        str_save = []
        if list_objs is not None:
            for obj in list_objs:
                str_save.append(obj.to_dictionary())
        str_save = cls.to_json_string(str_save)

        with open(cls.__name__ + ".json", mode="w") as a_file:
            a_file.write(str_save)
