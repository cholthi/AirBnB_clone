#!/usr/bin/env python3
"""Unit tests for BaseModels"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBEngine_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""
    def test_no_args_instantiates(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        len1 = len(models.storage.all())
        # Creating empty BaseModel calls new function
        bm1 = BaseModel()
        len2 = len(models.storage.all())
        self.assertLess(len1, len2)


if __name__ == "__main__":
    unittest.main()
