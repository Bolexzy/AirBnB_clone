#!/usr/bin/python3
"""
    Test suite for amenity.py
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.a = Amenity()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the Amenity class.
        """
        str_type = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), str_type)
        self.assertIsInstance(self.a, Amenity)
        self.assertTrue(issubclass(type(self.a), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class.
        """
        self.assertTrue(hasattr(self.a, 'name'))
        for k, v in vars(self.a).items():
            self.assertTrue(hasattr(self.a, k))


if __name__ == '__main__':
    unittest.main()
