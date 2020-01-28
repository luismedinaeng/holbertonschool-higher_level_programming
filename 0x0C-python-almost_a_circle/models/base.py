#!/usr/bin/python3
'''Module that has the Base Class for figures
'''
import json
import csv


class Base:
    '''Class that represents the base of a figure
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
        ''' Save to a file a list of objects in json format
        '''
        str_save = []
        if list_objs is not None:
            for obj in list_objs:
                str_save.append(obj.to_dictionary())
        str_save = cls.to_json_string(str_save)

        with open(cls.__name__ + ".json", mode="w") as a_file:
            a_file.write(str_save)

    @staticmethod
    def from_json_string(json_string):
        ''' Convert a string rep of a json to a list of dictionaries
        '''
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Create a object from a dictionary
        '''
        if cls.__name__ is "Rectangle":
            obj = cls(width=1, height=1)
        else:
            obj = cls(size=1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' Loads information from a json file and create a list of objects
        '''
        try:
            with open(cls.__name__ + ".json", mode="r") as a_file:
                str_load = a_file.read()
        except:
            str_load = ""
        str_load = cls.from_json_string(str_load)
        list_objs = []
        for obj in str_load:
            list_objs.append(cls.create(**obj))
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Save to a file a list of objects in csv format
        '''
        str_save = []
        if list_objs is not None:
            for obj in list_objs:
                str_save.append(obj.to_dictionary())

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        with open(cls.__name__ + ".csv", mode="w") as a_file:
            writ = csv.DictWriter(a_file, fieldnames=fields)
            writ.writeheader()
            for data in str_save:
                writ.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        ''' Loads information from a csv file and create a list of objects
        '''
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        str_load = []
        try:
            with open(cls.__name__ + ".csv", mode="r", newline="") as a_file:
                read_f = csv.DictReader(a_file)
                for obj in read_f:
                    obj_dict = dict(obj)
                    new_obj_dict = dict()
                    for k, v in obj_dict.items():
                        new_obj_dict[k] = int(v)
                    str_load.append(new_obj_dict)
        except:
            pass

        list_objs = []
        for obj in str_load:

            list_objs.append(cls.create(**obj))
        return list_objs
