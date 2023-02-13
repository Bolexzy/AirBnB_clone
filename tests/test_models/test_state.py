#!/usr/bin/python3
"""
    Test suite for state.py
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestState(unittest.TestCase):
    """Test cases for the State class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.s = State()

    def tearDown(self):
        """Tears down test methods.
        reset storage.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests for successful instantiation of the State class.
        """
        str_type = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), str_type)
        self.assertIsInstance(self.s, State)
        self.assertTrue(issubclass(type(self.s), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class.
        """
        self.assertTrue(hasattr(self.s, 'name'))
        for k, v in vars(self.s).items():
            self.assertTrue(hasattr(self.s, k))


if __name__ == '__main__':
    unittest.main()
