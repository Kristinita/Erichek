# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:32:05
# @Last Modified time: 2018-02-01 19:15:27
"""Run tests.

Main file for running Erichek tests.
"""

import erichek.eric_asterisks as eric_asterisks
import erichek.eric_body as eric_body
import erichek.eric_encoding as eric_encoding
import erichek.eric_head as eric_head
import logbook

from clize import run
from erichek.eric_config import clize_log_level
from erichek.eric_config import v
from erichek.eric_config import version

# Pyfancy — output color highighting
# Disabled green background, because bad color in AppVeyor
# https://github.com/appveyor/ci/issues/1138#issuecomment-355525721
# Import class, not a module
# https://stackoverflow.com/a/4534443/5951529
from pyfancy.pyfancy import pyfancy

# ASCII-art printing
# [BUG] ASCII-ART output, when --help or --version
# https://github.com/epsy/clize/issues/38#issue-290426111
# https://stackoverflow.com/a/9638532/5951529
# import sys
# from colorama import init
# from pyfiglet import figlet_format
# from termcolor import cprint

# strip colors if stdout is redirected
# init(strip=not sys.stdout.isatty())

LOG = logbook.Logger("summary logbook")


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


def main():
    """Run Erichek.

    Run all modules of Erichek.
    If no errors — validation success,
    Else — exit(1).
    """
    run(clize_log_level, alt=[version, v], exit=False)
    eric_encoding.eric_encoding_summary()
    eric_body.eric_body_summary()
    eric_asterisks.eric_asterisks_summary()
    eric_head.eric_head_summary()

    # If all instead of multiple if and:
    # https://stackoverflow.com/a/9504681/5951529
    if all([eric_body.BODY_EXIST, eric_encoding.ENCODING_WINDOWS_1251, eric_asterisks.ASTERISKS_EXISTS,
            eric_head.HEAD_DATA]):
        green_foreground(
            "Congratulations! You haven't errors in your packages!")
        # cprint(figlet_format('\nSuccess', font='starwars'),
        # 'white', 'on_green', attrs=['bold'])
    else:
        red_foreground(
            "You have errors in your packages. Please, fix them.")
        # cprint(figlet_format('\nFailure', font='starwars'),
        # 'yellow', 'on_red', attrs=['bold'])
        exit(1)


if __name__ == '__main__':
    main()
