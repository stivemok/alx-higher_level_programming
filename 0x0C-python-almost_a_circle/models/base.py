#!/usr/bin/python3
""" Base module"""
import json


class Base:
    """Base class
    "base" for all classess"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        id: id of new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the json string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == '[]':
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []
        if list_objs is None:
            jsonfile.write("[]")
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)
        with open(filename, 'w') as jsonfile:
            jsonfile.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """retuns list of json string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instancee with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []
        if filename is None:
            return []
        else:
            with open(filename, 'r') as jsonfile:
                list_dic = Base.from_json_string(jsonfile.read())
                for dic in list_dic:
                    return [cls.create(**dic)]
