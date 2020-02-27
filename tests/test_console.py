#!/usr/bin/python3
"""Test Console"""

import unittest
import pep8
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from models.review import Review


class Test_Console(unittest.TestCase):
    """Initial Test"""

    def test_Classes(self):
        """Test classes"""
        Statee = State()
        Cityy = City()
        Amenityy = Amenity()
        Placee = Place()
        Revieww = Review()
        self.assertEqual(Statee.__class__.__name__, "State")
        self.assertEqual(Cityy.__class__.__name__, "City")
        self.assertEqual(Amenityy.__class__.__name__, "Amenity")
        self.assertEqual(Placee.__class__.__name__, "Place")
        self.assertEqual(Revieww.__class__.__name__, "Review")
