#!/usr/bin/env python3
""" A  user class model """

from models.base_model import BaseModel


class User(BaseModel):
    """ A user class entity
      
        Attributes:
                email (str): The email of the user
                password (str): user password
                first_name (str): The first name of the user
                last_name  (str): The last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
