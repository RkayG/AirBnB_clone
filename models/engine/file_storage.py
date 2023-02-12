#!/usr/bin/python3
"""
Module - file_storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({"{}.{}".format(obj.__class__.__name__, obj.id): obj})

    def save(self):
        save_dict = {}
        for key, val in self.__objects.items():
            if type(val) is dict:
                save_dict[key] = val
            else:
                save_dict[key] = val.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(save_dict, file, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                reload_objs = json.load(file)
            for key, obj in reload_objs.items():
                self.__objects.update({key: (self.class_dict[obj['__class__']](**obj))})
        except FileNotFoundError:
            pass
