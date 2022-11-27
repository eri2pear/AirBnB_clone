#!/usr/bin/python3

"""Defining the amenity class inherited from the BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity module"""
    
    #Attributes
    name: str = ""
