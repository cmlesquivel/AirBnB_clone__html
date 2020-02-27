#!/usr/bin/python3
"""Test FileStorage"""
import unittest
from models.base_model import BaseModel
from models import storage
import pep8


class test_FileStorage(unittest.TestCase):
    """ Test FileStorage """

    def test_all(self):
        """Test all"""
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    def test_pep8_file_storage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, 'fix pep8')

if __name__ == '__main__':
    unittest.main()
