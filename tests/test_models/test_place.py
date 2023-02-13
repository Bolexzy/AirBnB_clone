#!/usr/bin/python3
"""
    Test suite for place.py
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):
    """Test cases for the Place class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.p = Place()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the Place class.
        """
        str_type = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.p)), str_type)
        self.assertIsInstance(self.p, Place)
        self.assertTrue(issubclass(type(self.p), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Place class.
        """
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        for k, v in vars(self.p).items():
            self.assertTrue(hasattr(self.p, k))


if __name__ == '__main__':
    unittest.main()
