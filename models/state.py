#!/usr/bin/python3
"""
    Defines a State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a class State.
     Inherits from BaseModel

    Attributes:
        name (str): The name of the state.
    """
    name = ""
