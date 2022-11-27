#!/usr/bin/python3

"""Defines a state module inherited from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State
    Attributes:
        name (str): name of the state.
    """

    name: str = ""
