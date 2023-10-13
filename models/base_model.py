#!/usr/bin/env python3
"""Defines BaseClass for all AirBnB model objects"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """represents base class for AirBnB model classes"""

    def __init__(self, *args, **kwargs):
        """Initializes all models for

           Args:
               *args (any): Variable arguments
               **kwargs (any): attributes for child classes
        """
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def to_dict(self):
        """Convert an instance of the model class to dict"""
        return_dict = self.__dict__.copy()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def save(self):
        """Saves the the model to the connected storage engine"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """Return a string representation for this BaseModel"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
