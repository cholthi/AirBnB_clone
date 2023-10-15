#!/usr/bin/env python3
"""The main console application AirBnB clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console command application interpreter"""
    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
