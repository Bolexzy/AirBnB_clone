#!/usr/bin/python3
"""
    Defines a Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review.
     Inherits from BaseModel

    Attributes:
        place_id (str): The review's place id.
        user_id (str): The review's user id.
        text (str): The review description.
    """
    place_id = ""
    user_id = ""
    text = ""
