#!/usr/bin/env python3
"""A file storage engine for AirBnB objects"""
import json


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
        self.__objects[obj.id] = obj

    def save(self):
        """Serializes objects"""
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(self.__objects)

    def reload(self):
        """Deserializes JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

