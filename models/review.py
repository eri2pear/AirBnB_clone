#!/usr/bin/python3

"""Defines a review module inherited from the Basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review
    Attributes:
        place_id (str): place_id of the Review
        user_id (str): user_id of the Review
        text (str): text of the Review
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
