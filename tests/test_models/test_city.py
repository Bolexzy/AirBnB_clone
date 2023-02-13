#!/usr/bin/python3
"""
    Test suite for city.py
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):
    """Test cases for the City class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.c = City()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the City class.
        """
        str_type = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.c)), str_type)
        self.assertIsInstance(self.c, City)
        self.assertTrue(issubclass(type(self.c), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class.
        """
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        for k, v in vars(self.c).items():
            self.assertTrue(hasattr(self.c, k))


if __name__ == '__main__':
    unittest.main()
