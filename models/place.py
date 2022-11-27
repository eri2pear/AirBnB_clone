#!/usr/bin/python3

"""Defines a place module, inherited from the Basemodel"""

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """Represents a Place
    Attributes:
        city_id (str): city_id of the Place.
        user_id (str): user_id of the Place.
        name (str): name of the Place.
        description (str): description of the Place.
        number_rooms (int): number_rooms of the Place.
        number_bathrooms (int): number_bathrooms of the Place.
        max_guest (int): max_guest of the Place.
        price_by_night (int): price_by_night of the Place.
        latitude (float): latitude of the Place.
        longitude (float): longitude of the Place.
        amenity_ids (array): amenity_ids of the Place.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []
