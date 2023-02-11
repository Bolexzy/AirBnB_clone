#!/usr/bin/python3
"""
    Defines an Amenity  class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity.
     Inherits from BaseModel

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
