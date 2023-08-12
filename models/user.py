#!/usr/bin/python3
"""This is the module that creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
