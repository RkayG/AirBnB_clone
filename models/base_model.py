#!/usr/bin/python3
"""
Module - base_model
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes attributes
        id, created_at and updated_at

        :param args:
        :param kwargs:
        """
        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints string representation of the class
        :return:
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        saves the class instance to a json file
        and updates the updated_at attribute
        :return:
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        creates a dictionary of the instance
        :return:
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(self.__class__.__name__)
        dictionary["id"] = str(self.id)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
