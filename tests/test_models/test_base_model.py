#!/usr/bin/python3
"""Test"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_BaseModel(unittest.TestCase):
    """Class test full"""

    def setUp(self):
        """sets up"""
        pass

    def test_pep8_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, 'fix pep8')

    def test_method(self):
        """Tests Methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_doc(self):
        """Test Docs"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        """Test save"""
        pass

if __name__ == '__main__':
    unittest.main()
