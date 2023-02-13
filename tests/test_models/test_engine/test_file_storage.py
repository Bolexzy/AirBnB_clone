#!/usr/bin/python3
"""
    Test suite for file_storage.py
"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os
import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class.
    """
    def setUp(self):
        """Sets up test methods."""
        self.base_model = BaseModel()

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
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_all(self):
        """Test public instance method all.
        """
        ret = FileStorage().all()
        self.assertIsInstance(ret, dict)

    def test_new(self):
        """Test public instance method new.
        """
        b = self.base_model
        FileStorage().new(b)
        key = f'{b.__class__.__name__}.{b.id}'
        self.assertEqual(FileStorage().all()[key], b)

    def test_save(self):
        """Test public instance method save.
        verify if json file exists.
        """
        self.base_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """
        """
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(storage.all()[key].to_dict(), value.to_dict())

    def test_attribute(self):
        """Tests the attributes of FileStorage class.
        """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)
        with self.assertRaises(AttributeError):
            file_path = FileStorage.__file_path
        with self.assertRaises(AttributeError):
            file_obj = FileStorage.__objects


if __name__ == '__main__':
    unittest.main()
