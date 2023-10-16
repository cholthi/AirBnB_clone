#!/usr/bin/env python3
"""Unit tests for city models"""
import unittest
from models.city import City
import models

TestCity_Instantiation(unittest.TestCase):
    """City model unit tests cases"""

    def test_instantiation_with_no_args(self):
        self.assertEqual(City, type(City()))

    def test_object_is_added_to_storage(self):
        self.assertIn(City(), models.storage.all().values())
