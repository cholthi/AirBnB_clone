#!/usr/bin/env python3
"""Unit tests for HBNBCommand console app"""

import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage

available_classes = classes = {'User', 'BaseModel', 'City',
                               'Review', 'Place', 'State', 'Amenity'}


class TestHBNBCmd_prompting(unittest.TestCase):
    def test_prompt(self):
        console = HBNBCommand()
        self.assertEqual("(hbnb) ", console.prompt)

    def test_empty_line(self):
        console = HBNBCommand()
        console.onecmd("")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_string_input(self):
        console = HBNBCommand()
        console.onecmd("some random string")
        self.assertEqual("(hbnb) ", console.prompt)


class TestHBNBCmd_exit(unittest.TestCase):
    def test_do_quit(self):
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))


class TestHBNBCmd_help(unittest.TestCase):
    """Unittest for testing help command and its arguments"""
    def test_do_help(self):
        """Tests the help command without arg"""
        hp = f"Documented commands (type help <topic>):\n"\
             "========================================\n"\
             "EOF  all  count  create  destroy  help  quit  show  update"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(hp, output.getvalue().strip())

    def test_do_help_EOF(self):
        """Tests help of EOF cmd"""
        hp_EOF = f"Exit program if EOF signal."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(hp_EOF, output.getvalue().strip())

    def test_do_help_quit(self):
        """Tests help of quit cmd"""
        hp_quit = f"Command to quit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hp_quit, output.getvalue().strip())

    def test_do_help_create(self):
        """Tests help of create cmd"""
        hp_create = f"Usage: create <class>\n"\
            "        Create a new class instance and print its id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(hp_create, output.getvalue().strip())

    def test_do_help_show(self):
        """Tests help of show cmd"""
        hp_show = f"Usage: show <class> <id> or <class>.show(<id>)\n"\
            "        Display the string representation of a "\
            "class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(hp_show, output.getvalue().strip())

    def test_do_help_destroy(self):
        """Tests help of destroy cmd"""
        hp_destroy = f"Usage: destroy <class> <id> or <class>.destroy(<id>)\n"\
            "        Delete a class instance of a given id."

    def test_do_help_all(self):
        """Tests help of all cmd"""
        hp_all = f"Usage: all or all <class> or <class>.all()\n"\
            "        Display string representations of all "\
            "instances of a given class.\n"\
            "        If no class is specified, displays all "\
            "instantiated objects."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(hp_all, output.getvalue().strip())

    def test_do_help_count(self):
        """Tests help of count cmd"""
        hp_count = f"Usage: count <class> or <class>.count()\n"\
            "        Retrieve the number of instances of "\
            "a given class."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertTrue(hp_count, output.getvalue().strip())

    def test_do_help_update(self):
        """Tests help update cmd"""
        hp_update = f"Usage: update <class> <id> <attribute_name> "\
            "<attribute_value> or\n"\
            "       <class>.update(<id>, <attribute_name>, "\
            "<attribute_value>) or\n"\
            "       <class>.update(<id>, <dictionary>)\n"\
            "        Update a class instance of a given id by"\
            " adding or updating\n"\
            "        a given attribute key/value pair or dictionary."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(hp_update, output.getvalue().strip())


class TestHBNBCmd_create(unittest.TestCase):
    """Unittest for testing create command and its args"""
    @classmethod
    def setUpClass(cls):
        """Executed before any of the tests are run"""
        try:
            os.rename("data.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Executed after all the tests have run"""
        try:
            os.remove("data.json")
        except IOError:
            pass
        try:
            os.rename("temp", "data.json")
        except IOError:
            pass

    def test_do_create_object(self):
        """Tests for create method creating an object"""
        for clss in available_classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(
                    "create {}".format(clss)))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "{}.{}".format(clss, output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())

    def test_do_create_missing_class(self):
        """Tests do_create where class is missing"""
        st = f"** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd("create"))
            self.assertTrue(st, output.getvalue().strip())

    def test_do_create_invalid_class(self):
        """Tests do_create where class is invalid"""
        st = f"** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd("create .InvalidClass"))
            self.assertEqual(st, output.getvalue().strip())

    def test_do_create_invalid_syntax(self):
        """Tests do_create where syntax is invalid"""
        st = f"*** Unknown syntax: .create."
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd(".create. "))
            self.assertEqual(st, output.getvalue().strip())


class TestHBNBCmd_update(unittest.TestCase):
    """Unittest for testing update command and its args"""
    @classmethod
    def setUpClass(cls):
        """Executed before any of the tests are run"""
        try:
            os.rename("data.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Executed after all the tests have run"""
        try:
            os.remove("data.json")
        except IOError:
            pass
        try:
            os.rename("temp", "data.json")
        except IOError:
            pass

    def test_do_update_missing_arguments(self):
        """Tests do_update where class is missing"""
        st = f"** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd("create"))
            self.assertTrue(st, output.getvalue().strip())

    def test_update_missing_id(self):
        """Tests update for unavailable id
        """
        st = f"** instance id missing **"
        for clss in available_classes:
            # update lacks id in argument case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update {}".
                                                      format(clss)))
                self.assertEqual(st, output.getvalue().strip())
            # update lacks id for dot notation case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("{}.update()".
                                                      format(clss)))
                self.assertEqual(st, output.getvalue().strip())

    def test_update_invalid_id(self):
        """Tests update for unavailable id
        """
        st = f"** no instance found **"
        for clss in available_classes:
            # update lacks id in argument case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update {} 3".
                                                      format(clss)))
                self.assertEqual(st, output.getvalue().strip())
            # update lacks id for dot notation case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("{}.update(3)".
                                                      format(clss)))
                self.assertEqual(st, output.getvalue().strip())

    def test_update_missing_attr_name(self):
        """Tests update for missing attribute name
        """
        st = f"** attribute name missing **"
        for clss in available_classes:
            # update lacks id in argument case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create {}".
                                                      format(clss)))
                testId = output.getvalue().strip()
                testCmd = "update {} {}".format(clss, testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(st, output.getvalue().strip())
            # update lacks id for dot notation case
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create {}".
                                                      format(clss)))
                testId = output.getvalue().strip()
                testCmd = "{}.update({})".format(clss, testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(st, output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        """Tests update for missing attribute value"""
        st = f"** value missing **"
        for clss in available_classes:
            # update lacks id in argument case
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(clss))
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update {} {} attr_name".format(clss, testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(st, output.getvalue().strip())
            # update lacks id for dot notation case
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(clss))
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "{}.update({}, attr_name)".format(clss, testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(st, output.getvalue().strip())

    def test_update_valid_int(self):
        """Tests update for valid int"""
        # update lacks id in argument case
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} max_guest 20".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(20, test_dict["max_guest"])

        # update lacks id for dot notation case
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 20)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(20, test_dict["max_guest"])

    def test_update_valid_string_attr(self):
        """Tests update for valid string"""
        for clss in available_classes:
            # update lacks id in argument case
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(clss))
                testId = output.getvalue().strip()
            testCmd = "update {} {} attr_name 'attr_value'".format(
                clss, testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["{}.{}".format(clss, testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])
            # update lacks id for dot notation case
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(clss))
                tId = output.getvalue().strip()
            testCmd = "{}.update({}, attr_name, 'attr_value')".format(
                clss, tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["{}.{}".format(clss, tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_do_create_invalid_syntax(self):
        """Tests do_update where syntax is invalid"""
        st = f"*** Unknown syntax: .create."
        with patch("sys.stdout", new=StringIO()) as output:
            console = HBNBCommand()
            self.assertFalse(console.onecmd(".create. "))
            self.assertEqual(st, output.getvalue().strip())


class TestHBNBCmd_show(unittest.TestCase):
    def test_do_show_missing_arguments(self):
        console = HBNBCommand()
        console.onecmd("show")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_do_show_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("show InvalidClass 1234-1234-1234")
        self.assertEqual("(hbnb) ", console.prompt)


class TestHBNBCmd_all(unittest.TestCase):
    def test_do_all_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("all InvalidClass")
        self.assertEqual("(hbnb) ", console.prompt)


class TestHBNBCmd_destroy(unittest.TestCase):
    def test_do_destroy_missing_arguments(self):
        console = HBNBCommand()
        console.onecmd("destroy")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_do_destroy_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("destroy InvalidClass 1234-1234-1234")
        self.assertEqual("(hbnb) ", console.prompt)


if __name__ == '__main__':
    unittest.main()

