# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-02 08:35:59
# @Last Modified time: 2019-05-06 10:37:04
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
# I'm create a junction via junction, that works in convenient location:
# https://superuser.com/a/1020825/572069
import glob
import os
import platform
import sys
import traceback

import delegator
# logbook — custom logging:
# http://logbook.readthedocs.io/en/stable/quickstart.html
# Set NOTICE level:
# https://github.com/search?q=StreamHandler(sys.stdout).push_application()&type=Code
import logbook
import pkg_resources
import pyperclip


# Pyfancy — output color highighting
# Disabled green background, because bad color in AppVeyor
# https://github.com/appveyor/ci/issues/1138#issuecomment-355525721
# Import class, not a module
# https://stackoverflow.com/a/4534443/5951529
# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from pyfancy.pyfancy import pyfancy
from sorcery import switch

# Get all .txt file in a directory
# https://stackoverflow.com/a/3964689/5951529
# «glob.glob('../*.txt')» in parent folder, not «glob.glob('../*.txt')»!
# Recursive since Python 3.5:
# https://stackoverflow.com/a/2186565/5951529
ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS = glob.glob(
    '**/*.txt', recursive=True)


def eric_opened_files():
    """Get list all filenames in a working directory.

    Get list of all filenames and strip paths.

    Yields:
        list -- filenames in working directory

    """
    for filename_pylint in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:
        # Check if string in a file
        # https://stackoverflow.com/a/4944929/5951529
        # Encoding for Travis CI, see
        # https://stackoverflow.com/a/31492722/5951529
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354674238
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354681085
        # Open file:
        # https://stackoverflow.com/a/3277515/5951529
        # “with open” better, because file properly closed, even an exception:
        # https://stackoverflow.com/a/36860392/5951529
        with open(filename_pylint, "r", encoding='utf-8') as unhandled_file:
            # File as string:
            # https://stackoverflow.com/a/16082963/5951529
            file_as_string = unhandled_file.read()
            # print("unhandled_file", type(unhandled_file))
            # print("file_as_string", type(file_as_string))
            yield filename_pylint, file_as_string


def version():
    """Copy to clipboard OS, Python and erichek information.

    https://stackoverflow.com/a/11063483/5951529

    For version details see:
    https://clize.readthedocs.io/en/stable/dispatching.html#alternate-actions

    OS information:
    https://stackoverflow.com/a/10091465/5951529
    OS architecture:
    https://stackoverflow.com/a/45659845/5951529
    Get Python version:
    https://stackoverflow.com/a/41588204/5951529
    Node version via delegator.py:
    https://github.com/kennethreitz/delegator.py
    Package version:
    https://stackoverflow.com/a/20683902/5951529

    Example output:

    # Environment

    + Windows 64bit 10.0.14393,
    + Python 3.7.0,
    + Node.js v10.4.1,
    + Erichek 0.3.2.
    """
    erichek_metadata = pkg_resources.get_distribution('Erichek')
    erichek_version = erichek_metadata.version
    pyperclip.copy(
        '### Environment\n\n'
        '+ ' + platform.system() + ' ' +
        platform.architecture()[0] + ' ' +
        platform.version() + '\n' +
        '+ Python ' + platform.python_version() + '\n' +
        '+ Node.js ' + delegator.run('node -v').out +
        '+ Erichek ' + erichek_version + '.'
    )

# [DEPRECATED] Pylint check, that is incorrect function name
# http://pylint-messages.wikidot.com/messages:c0103
# def v():
#     Alternative show version.

#     For details see: https://github.com/epsy/clize/issues/34

#     version()


def logbook_initial(level):
    """Define Logbook levels.

    User select, which logging messages to see. See about 6 log levels here:
    https://logbook.readthedocs.io/en/stable/quickstart.html

    Arguments:
        level {int} -- Logbook level
    """
    logbook.StreamHandler(sys.stdout, level).push_application()


def eric_logbook_critical():
    """Critical level."""
    logbook_initial(logbook.CRITICAL)


def eric_logbook_error():
    """Error level."""
    logbook_initial(logbook.ERROR)


def eric_logbook_warning():
    """Warning level."""
    logbook_initial(logbook.WARNING)


def eric_logbook_notice():
    """Notice level."""
    logbook_initial(logbook.NOTICE)


def eric_logbook_info():
    """Info level."""
    logbook_initial(logbook.INFO)


def eric_logbook_debug():
    """Debug level."""
    logbook_initial(logbook.DEBUG)

# Mypy not support Clize syntax:
# https://github.com/python/mypy/issues/5541
# Ignoring in Mypy:
# https://github.com/python/mypy/issues/500#issuecomment-87460993


def clize_log_level(*, logbook_level: 'll' = "NOTICE"):  # noqa type: ignore
    """Change log levels via command line.

    if/elif/else simplified entry:
    https://ru.stackoverflow.com/a/873470/199934

    :param logbook_level: user select logging level
    """
    # Disable specific Pylint rule for block:
    # https://stackoverflow.com/a/24672552/5951529
    # Pylint unsupport sorcery switch syntax:
    # https://github.com/PyCQA/pylint/issues/2450
    # pylint: disable=E1120
    switch(logbook_level, lambda: {
        "DEBUG": eric_logbook_debug(),
        "INFO": eric_logbook_info(),
        "ERROR": eric_logbook_error(),
        "NOTICE": eric_logbook_notice(),
        "WARNING": eric_logbook_warning(),
        "CRITICAL": eric_logbook_critical()
    })
    # pylint: enable=E1120


def logger_function():
    """Show module names in Logbook description.

    Use switch module of sorcery package for replace multiple “if”:
    https://github.com/alexmojaki/sorcery#switch
    [NOTE] Don't use default value in this case!

    It replace:
    if logbook_level == "DEBUG":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.DEBUG).push_application()
    elif logbook_level == "INFO":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.INFO).push_application()

    Needs function, not variable, because the value is determined at the time of the call,
    and not the import of the module.
    https://ru.stackoverflow.com/questions/872316/#comment1416313_872340

    Returns:
        {class} -- module name, that pass logs

    """
    return logbook.Logger(os.path.splitext(
        os.path.basename(traceback.extract_stack()[-3].filename))[0])


def pyfancy_function(level_argument, pyfancy_wrapper, pyfancy_variable):
    """Wrap Pyfancy statements.

    Wrap function for colors.

    Arguments:
        level_argument {func} -- Logbook level, debug, notice etc.
        pyfancy_wrapper {func} -- colors and bold for logging text
        pyfancy_variable {str} -- logging text
    """
    level_argument(pyfancy_wrapper.add(pyfancy_variable))

# pylint: disable=E1101
# Pylint unsupport pyfancy syntax:
# https://github.com/PyCQA/pylint/issues/2448


def pyfancy_critical(pyfancy_variable):
    """Critical level."""
    pyfancy_function(
        logger_function().critical,
        pyfancy().red_bg().bold(),
        pyfancy_variable)


def pyfancy_error(pyfancy_variable):
    """Error level."""
    pyfancy_function(
        logger_function().error,
        pyfancy().red().bold(),
        pyfancy_variable)


def pyfancy_warning(pyfancy_variable):
    """Error level."""
    pyfancy_function(
        logger_function().warning,
        pyfancy().yellow().bold(),
        pyfancy_variable)


def pyfancy_notice(pyfancy_variable):
    """Notice level."""
    pyfancy_function(
        logger_function().notice,
        pyfancy().green().bold(),
        pyfancy_variable)

# pylint: enable=E1101


def pyfancy_debug(pyfancy_variable):
    """Debug level (no text decoration)."""
    pyfancy_function(logger_function().debug, pyfancy(), pyfancy_variable)
