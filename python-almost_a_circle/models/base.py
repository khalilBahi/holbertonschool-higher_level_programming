#!/usr/bin/python3
"""
module Base class
"""
import json
from os.path import isfile


class Base:
    """This class will be the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(size=3)
        elif cls.__name__ == "Rectangle":
            dummy = cls(height=3, width=5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                list = cls.from_json_string(json_string)
                return [cls.create(**dict_data) for dict_data in list]
        else:
            return []
