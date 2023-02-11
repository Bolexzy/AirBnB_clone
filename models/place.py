#!/usr/bin/python3
"""
    Defines a  Place class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place.
     Inherits from BaseModel

    Attributes:
        city_id (str): The place's city id(City.id).
        user_id (Str): The places's user id (User.id).
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The Place's price by night.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids (list): An id list of all linked amenities(Amenity.id).
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
