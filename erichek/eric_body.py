# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:23:52
# @Last Modified time: 2018-09-03 14:50:16
"""Check files for body.

Check, contains files of directory <body> or no.
"""
from erichek.eric_config import eric_opened_files
from erichek.eric_config import pyfancy_critical
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_notice


def eric_body_function():
    """Check, contains body in a file, or no."""
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_without_path, pylint_as_string in eric_opened_files():
        if "<body>" in pylint_as_string:
            pyfancy_debug(f"{filename_without_path}: <body> exists")
        else:
            pyfancy_critical(
                f"{filename_without_path}: <body> not exists. Please, add <body> to {filename_without_path}.")
            # Multiline f-strings:
            # https://realpython.com/python-f-strings/#multiline-f-strings
            pyfancy_notice(
                f"If you see this message and, possibly, long red output after them, "
                f"your file {filename_without_path} not contains <body>. "
                f"Please, add <body> to {filename_without_path} to correct place and rerun Erichek.")
            yield False
