#!/usr/bin/env python3
"""Unit testing user model"""

import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Tests user model"""
    def setUp(self):
        """Creates instance of user class"""
        self.user = User()
    def test_instance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_user_name(self):
        """Tests user name"""
        self.assertEqual(str, type(self.user.first_name))
        self.assertEqual(str, type(self.user.last_name))
        
    def test_parent_property_created_at(self):
        """Test time created"""
        self.assertEqual(datetime, type(self.user.created_at))
    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.user, models.storage.all().values())

if __name__ == "__main__":
    unittest.main()