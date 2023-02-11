#!/usr/bin/python3
"""
    Defines a City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a class, City.
     Inherits from BaseModel

    Attributes:
        name (str): The name of the city.
        state_id (str): The id of the state(state.id).
    """

    state_id = ""
    name = ""
