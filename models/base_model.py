#!/usr/bin/python3
"""
    Defines a BaseModel class.
"""
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes & methods for other classes.

    Attributes:
        id (str): The unique id of an instance.
        created_at (datetime): The current datetime at creation.
        updated_at (datetime): The current datetime of last update/change.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.
        """
        if not kwargs and kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns the string representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, obj_dict)

    def save(self):
        """Updates the instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = str(type(self).__name__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return (obj_dict)
