#!/usr/bin env python3
"""Defines attributes/methods for User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class user of project
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
