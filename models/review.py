#!/usr/bin env python3
"""Defines attributes/methods for Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class of project
    """

    place_id = ""
    user_id = ""
    text = ''
