#!/usr/bin/env python3
"""Unit tests for HBNBCommand console app"""

import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


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
    def test_do_create_object(self):
        """Tests do_create an object"""
        pass


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
    def test_do_update_missing_arguments(self):
        console = HBNBCommand()
        console.onecmd("update")
        self.assertEqual("(hbnb) ", console.prompt)

    def test_do_update_invalid_class(self):
        console = HBNBCommand()
        console.onecmd("update InvalidClass 1234-1234-1234")
        self.assertEqual("(hbnb) ", console.prompt)


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
