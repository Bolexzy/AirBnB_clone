#!/usr/bin/python3
"""
    Test suite for user.py
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.u = User()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the User class.
        """
        str_type = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.u)), str_type)
        self.assertIsInstance(self.u, User)
        self.assertTrue(issubclass(type(self.u), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class.
        """
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        for k, v in vars(self.u).items():
            self.assertTrue(hasattr(self.u, k))


if __name__ == '__main__':
    unittest.main()
