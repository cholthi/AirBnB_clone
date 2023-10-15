#!/usr/bin/env python3
"""Unit testing user model"""

import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from models.city import City

class TestUser(unittest.TestCase):
    """Tests user model"""
    def setUp(self):
        """Creates instance of user class"""
        self.city = City()
        self.storedData = models.storage.all()
        self.className = self.city.__class__.__name__

    def test_instance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_city_name(self):
        """Tests user name"""
        self.assertEqual(str, type(self.city.name))
        self.assertEqual(str, type(self.city.state_id))

        self.assertEqual("", self.storedData[f"{self.className}.{self.city.id}"].name)
        
    def test_parent_property_created_at(self):
        """Test time created"""
        self.assertEqual(datetime, type(self.city.created_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.city, self.storedData.values())

if __name__ == "__main__":
    unittest.main()