# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 18:30:38
# @Last Modified time: 2019-05-04 08:11:18
"""Encoding checker.

Check, that files in Windows-1251 encoding.

Bugs:
    1. if no Cyrillic symbols in a file, chardet detect file encoding as ASCII;
    2. chardet can detect Windows-1251 as MacCyrillic.
"""
import codecs

import chardet

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS
from erichek.eric_config import pyfancy_critical
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_notice

# [DEPRECATED] Use yield and return for variables passing.
# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529


def eric_encoding_function():
    """Check encoding of the file.

    chardet check, that each file in Windows-1251.
    MacCyrillic — also true.
    In local testing UTF-8 convert to Cyrillic-1251.
    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_pylint in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:

        # Chardet not 100% accuracy guarantees:
        # https://stackoverflow.com/a/436299/5951529
        # Check:
        # https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function
        # https://stackoverflow.com/a/37531241/5951529
        # r+b mode is open the binary file in read or write mode.
        # https://stackoverflow.com/a/15746971/5951529
        with codecs.open(filename_pylint, "r+b") as opened_file:
            bytes_file = opened_file.read()
            chardet_data = chardet.detect(bytes_file)
            fileencoding = (chardet_data['encoding'])

            # [DEPRECATED] Migrating from Cyrillic 1251 to UTF-8
            # Needs MacCyrillic, because chardet can check Windows-1251
            # as MacCyrillic
            if fileencoding == 'utf-8':
                pyfancy_debug(f"{filename_pylint}: UTF-8 encoding")
            else:
                # Decode:
                # https://stackoverflow.com/a/38102444/5951529
                # Encode:
                # https://stackoverflow.com/a/37376668/5951529
                encoded_file = bytes_file.decode(fileencoding).encode()
                pyfancy_critical(f"{filename_pylint}: {fileencoding} encoding, not UTF-8!")
                pyfancy_notice(f"{filename_pylint}: encoding automatically converted from {fileencoding} to UTF-8")
                # Seek:
                # https://stackoverflow.com/a/2424410/5951529
                # https://stackoverflow.com/a/11696554/5951529
                opened_file.seek(0)
                opened_file.write(encoded_file)
                # Doesn't need truncate in write mode:
                # https://stackoverflow.com/a/4562477/5951529
                yield False
