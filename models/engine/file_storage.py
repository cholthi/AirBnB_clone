#!/usr/bin/env python3
"""A file storage engine for AirBnB objects"""
import json
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user  import User
from models.place import Place
from models.review import Review


class FileStorage:
    """A file storage engine for AirBnB clone project"""

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return self.__objects

    def new(self, obj):
        """Creates new object

        Args:
            obj (any): new object (with key <obj class name>.id)
            to store.
        """
        obj_id = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_id] = obj

    def save(self):
        """Serializes objects"""
        store_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(store_dict, f)

    def reload(self):
        """Deserializes JSON file to model objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objdict = json.load(f)
                for id, clsdict in objdict.items():
                    clsname = clsdict["__class__"]
                    del clsdict["__class__"]
                    self.new(eval(clsname)(**clsdict))
        except FileNotFoundError:
            pass

