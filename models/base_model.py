#!/usr/bin env python3
"""Defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Class base of project
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        """

        formato = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    setattr(self, key, datetime.strptime(value, formato))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(value, formato))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return
        """
        style = '[{}] ({}) {}'
        return(style.format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """Return
        """
        style = '[{}] ({}) {}'
        return(style.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        my_dict = self.__dict__.copy()

        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return(my_dict)
