#!/usr/bin/python3
"""
Test
"""
import unittest
from models import storage
import pep8
import os
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    """Class test full"""

    def setUp(self):
        """Test Set up"""
        pass

    def test_pep8_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, 'fix pep8')

    def test_1(self):
        """Test_1"""
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    def test_2(self):
        """Test_2"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertIsNotNone(hasattr(Review, "user_id"))


if __name__ == '__main__':
    unittest.main()
