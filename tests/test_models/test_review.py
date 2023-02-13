#!/usr/bin/python3
"""
    Test suite for review.py
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """Test cases for the Review class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.r = Review()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the Review class.
        """
        str_type = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), str_type)
        self.assertIsInstance(self.r, Review)
        self.assertTrue(issubclass(type(self.r), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class.
        """
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        for k, v in vars(self.r).items():
            self.assertTrue(hasattr(self.r, k))


if __name__ == '__main__':
    unittest.main()
