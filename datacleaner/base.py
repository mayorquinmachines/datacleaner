import sys
import os
import socket
import shutil
import argparse

from .dir import DirManager


PACKAGE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEMPLATES_PATH = os.path.join(PACKAGE_PATH, 'templates')


def execute_from_command_line():
    """
    Function linked to datacleaner terminal command.
    """
    commands = {
            'clean': DirManager,
                }

    args = sys.argv[:]
    command_text = args[1]

    if command_text in commands.keys():
        command = commands[command_text]
        c = command()
        c.run(args[2:])
    else:
        print('Usage: The availible commands are:')
        print(list(commands.keys()))



