#!/usr/bin/python3

"""Defines a user module inherited from the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): email of the user.
        password (str): password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
