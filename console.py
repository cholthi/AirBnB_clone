#!/usr/bin/env python3
"""The main console application AirBnB clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console command application interpreter"""
    prompt = "(hbnb) "


    def do_quit(self, line):
        """Command to quit the program

        Args:
            line (args): cmd line argument to quit the program
        """
        return True
    
    def emptyline(self):
        """Do nothing if empty line is received."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()