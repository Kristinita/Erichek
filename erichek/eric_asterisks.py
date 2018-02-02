# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 19:58:48
# @Last Modified time: 2018-02-02 08:37:57
"""Asterisks Checker.

Check, if asterisks contains in each line of package for Eric room.

Do not check:
    1. lines before <body> and line with <body>,
    2. <!-- comments -->.
"""
import logbook

import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from pyfancy.pyfancy import pyfancy

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS


LOG = logbook.Logger("eric_asterisks logbook")

ASTERISKS_EXISTS = True


def red_foreground(redtext):
    """Red foreground for error messages.

    Red foreground for error messages.

    Arguments:
        redtext {str} -- text, which will be colored in red.
    """
    LOG.error(pyfancy().red().bold(redtext))


def green_foreground(greentext):
    """Green foreground for notice messages.

    Green foreground for error messages.

    Arguments:
        greentext {str} -- text, which will be colored in green.
    """
    LOG.notice(pyfancy().green().bold(greentext))


def eric_asterisks_function():
    """Check, contains asterisks in each line of a file, or no."""
    for filename in ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS:

        filename_without_path = os.path.basename(filename)
        # Lines to list
        # https://stackoverflow.com/a/3277515/5951529
        with open(filename, encoding='windows-1251') as filename_as_list:
            submit_file_as_list = filename_as_list.readlines()
            # New list after <body>
            # https://stackoverflow.com/a/35880897/5951529
            # Except: if <body> not contains, Erichek output ValueError.
            # Propose to add <body>.
            try:
                get_lines_with_body = submit_file_as_list.index('<body>\n')
                list_without_lines_with_body = submit_file_as_list[
                    get_lines_with_body + 1:]
            except ValueError:
                green_foreground("If you see this message and, possibly, long output after them, "
                                 "your file " + filename_without_path + " not contains <body>. "
                                 "Please, add <body> to " + filename_without_path + " to correct place "
                                 "and rerun erichek.")
                # Check, that asterisks contains in full file
                list_without_lines_with_body = submit_file_as_list

            # Remove list item, contains «<!--»
            # https://stackoverflow.com/a/3416473/5951529
            list_without_lines_with_body_and_comments = [x for x in
                                                         list_without_lines_with_body if '<!--' not in x]
            # Check all elements of list, that contains «*»
            # https://stackoverflow.com/a/44118151/5951529
            # List comprehension: print incorrect list items
            # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
            if all('*' in item for item in list_without_lines_with_body_and_comments):
                LOG.debug(
                    "All lines in " +
                    filename_without_path +
                    " contains asterisks")
            else:
                lines_without_asterisks = [item for item in
                                           list_without_lines_with_body_and_comments if '*' not in
                                           item]
                # Remove \n symbol in end of the lines
                # https://stackoverflow.com/a/30881893/5951529
                lines_without_asterisks_and_n = list(
                    map(str.strip, lines_without_asterisks))
                # Lists to strings with quotes
                # https://stackoverflow.com/a/13207725/5951529
                lines_without_asterisks_and_n_as_strings = str(
                    lines_without_asterisks_and_n)[1:-1]
                red_foreground("This line(s) not contains asterisks: " +
                               lines_without_asterisks_and_n_as_strings +
                               " in " +
                               filename_without_path)
                global ASTERISKS_EXISTS
                ASTERISKS_EXISTS = False


def eric_asterisks_summary():
    """Report, contains asterisks in all files or no."""
    eric_asterisks_function()
    if ASTERISKS_EXISTS:
        green_foreground("All needest lines contains asterisks")

    if not ASTERISKS_EXISTS:
        red_foreground(
            "One or more your files not contained asterisks. Please, correct your package.")
