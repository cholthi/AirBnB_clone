#!/usr/bin/env python3
""" A state class enity """
from models.base_model import BaseModel

class State(BaseModel):
    """ A class representing state
       
       Attributes:
                name (str): the name of the state
    """
    name = ""
