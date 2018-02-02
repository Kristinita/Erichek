# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:35:59
# @Last Modified time: 2018-01-26 17:30:14
# For pydocstyle:
# D301: Use r""", if any backslashes in a docstring
r"""Patorjk-HeX ASCII-art font.

        _____                                                                                _____
   _____\    \ ___________        ____________         _____         __     __          _____\    \  ______   _______
  /    / |    |\          \      /            \   _____\    \_      /  \   /  \        /    / |    ||\     \  \      \
 /    /  /___/| \    /\    \    |\___/\  \\___/| /     /|     |    /   /| |\   \      /    /  /___/| \\     \  |     /|
|    |__ |___|/  |   \_\    |    \|____\  \___|//     / /____/|   /   //   \\   \    |    |__ |___|/  \|     |/     //
|       \        |      ___/           |  |    |     | |____|/   /    \_____/    \   |       \         |     |_____//
|     __/ __     |      \  ____   __  /   / __ |     |  _____   /    /\_____/\    \  |     __/ __      |     |\     \
|\    \  /  \   /     /\ \/    \ /  \/   /_/  ||\     \|\    \ /    //\_____/\\    \ |\    \  /  \    /     /|\|     |
| \____\/    | /_____/ |\______||____________/|| \_____\|    |/____/ |       | \____\| \____\/    |  /_____/ |/_____/|
| |    |____/| |     | | |     ||           | /| |     /____/||    | |       | |    || |    |____/| |     | / |    | |
 \|____|   | | |_____|/ \|_____||___________|/  \|_____|    |||____|/         \|____| \|____|   | | |_____|/  |____|/
       |___|/                                          |____|/                              |___|/
"""

# Configuration Erichek file.
# Imports and variables for Erichek.

import glob

# logbook — custom logging:
# http://logbook.readthedocs.io/en/stable/quickstart.html
# Set NOTICE level:
# https://github.com/search?q=StreamHandler(sys.stdout).push_application()&type=Code
import logbook
import sys

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
# «glob.glob('../*.txt')» in parent folder, not «glob.glob('../*.txt')»!
ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS = glob.glob('./*.txt')

VERSION = "0.1"


def version():
    """Show version.

    For details see:
    https://clize.readthedocs.io/en/stable/dispatching.html#alternate-actions
    """
    print(VERSION)


def v():
    """Alternative show version.

    For details see: https://github.com/epsy/clize/issues/34
    """
    print(VERSION)


def clize_log_level(*, logbook_level: 'll'="NOTICE"):
    """Change log levels via command line.

    User select, which logging messages to see. See about 6 log levels here:
    https://logbook.readthedocs.io/en/stable/quickstart.html

    :param logbook_level: user select logging level
    """
    if logbook_level == "DEBUG":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.DEBUG).push_application()
    elif logbook_level == "INFO":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.INFO).push_application()
    elif logbook_level == "NOTICE":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()
    elif logbook_level == "WARNING":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.WARNING).push_application()
    elif logbook_level == "ERROR":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.ERROR).push_application()
    elif logbook_level == "CRITICAL":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.CRITICAL).push_application()
    else:
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()
