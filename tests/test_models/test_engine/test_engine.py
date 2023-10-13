#!/usr/bin/env python3
"""Unit tests for BaseModels"""
import unittest
from models.engine.file_storage import FileStorage




class TestBEngine_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_no_args_instantiates(self):
        self.assertEqual(FileStorage, type(FileStorage()))


if __name__ == "__main__":
    unittest.main()