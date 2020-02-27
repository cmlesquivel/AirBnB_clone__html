#!/usr/bin env python3
"""Defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to variable __objects
        """

        key = obj.__class__.__name__ + '.' + obj.id
        value = obj.to_dict()
        my_new_obj = FileStorage.__objects.setdefault(key, obj)

    def save(self):
        """serializes __objects to the JSON file
        """

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        my_json = json.dumps(new_dict)

        with open(FileStorage.__file_path, 'w') as file:
            file.write(my_json)

    def reload(self):
        """deserializes the JSON file to __objects
        """

        myCls = {'BaseModel': BaseModel, 'User': User, 'State': State,
                 'City': City, 'Amenity': Amenity, 'Place': Place,
                 'Review': Review}
        cl = '__class__'

        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    if value[cl] in myCls:
                        FileStorage.__objects[key] = myCls[value[cl]](**value)
        except FileNotFoundError:
            pass
