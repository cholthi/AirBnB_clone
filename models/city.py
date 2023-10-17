#!/usr/bin/python3
""" A city class entity """
from models.base_model import BaseModel


class City(BaseModel):
    """City model class

       Attributes:
               state_id (str): State where city is found in
               name (str): The city name
    """
    state_id = ""
    name = ""
