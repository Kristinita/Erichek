# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-26 10:06:04
# @Last Modified time: 2018-01-27 07:40:52
"""Check files for correct head metadata.

Check, that files contains «Описание пакета:», «Процесс тренировки:» and so on.
"""
import logbook

import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from pyfancy.pyfancy import pyfancy

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS
LOG = logbook.Logger("eric_head logbook")

HEAD_DATA = True

# Multiple True
# https://stackoverflow.com/a/11717045/5951529
DESCRIPTION_FAILURE_TESTS, TRAINING_PROCESS_FAILURE_TESTS, FIRST_EXAMPLE_FAILURE_TESTS, \
    FIRST_ANSWER_FAILURE_TESTS, SECOND_EXAMPLE_FAILURE_TESTS, SECOND_ANSWER_FAILURE_TESTS, \
    PROOFS_FAILURE_TESTS, AUTHORS_FAILURE_TESTS, LINK_FAILURE_TESTS, PACKAGE_LINK_FAILURE_TESTS = (
        True,) * 10


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


def eric_head_function():
    """Check, that files contains metadata.

    Check for next metadata:

        + Описание пакета:
        + Процесс тренировки:
        + Примечания:
        + Пример вопроса 1:
        + Ответ к примеру вопроса 1:
        + Пример вопроса 2:
        + Ответ к примеру вопроса 2:
        + Источник(и):
        + Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):
        + Ссылка(и) на источник(и):
        + Постоянный адрес пакета:
    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename in ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS:

        filename_without_path = os.path.basename(filename)

        # File content in folder
        each_file_in_folder = open(filename, encoding='windows-1251').read()

        # Find head data
        if 'Описание пакета:' in each_file_in_folder:
            LOG.debug(
                '«Описание пакета:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Описание пакета:»')
            global DESCRIPTION_FAILURE_TESTS
            DESCRIPTION_FAILURE_TESTS = False

        if 'Процесс тренировки:' in each_file_in_folder:
            LOG.debug(
                '«Процесс тренировки:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Процесс тренировки:»')
            global TRAINING_PROCESS_FAILURE_TESTS
            TRAINING_PROCESS_FAILURE_TESTS = False

        if 'Пример вопроса 1:' in each_file_in_folder:
            LOG.debug(
                '«Пример вопроса 1:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Пример вопроса 1:»')
            global FIRST_EXAMPLE_FAILURE_TESTS
            FIRST_EXAMPLE_FAILURE_TESTS = False

        if 'Ответ к примеру вопроса 1:' in each_file_in_folder:
            LOG.debug(
                '«Ответ к примеру вопроса 1:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Ответ к примеру вопроса 1:»')
            global FIRST_ANSWER_FAILURE_TESTS
            FIRST_ANSWER_FAILURE_TESTS = False

        if 'Пример вопроса 2:' in each_file_in_folder:
            LOG.debug(
                '«Пример вопроса 2:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Пример вопроса 2:»')
            global SECOND_EXAMPLE_FAILURE_TESTS
            SECOND_EXAMPLE_FAILURE_TESTS = False

        if 'Ответ к примеру вопроса 2:' in each_file_in_folder:
            LOG.debug(
                '«Ответ к примеру вопроса 2:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Ответ к примеру вопроса 2:»')
            global SECOND_ANSWER_FAILURE_TESTS
            SECOND_ANSWER_FAILURE_TESTS = False

        if 'Источник(и):' in each_file_in_folder:
            LOG.debug(
                '«Источник(и):» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Источник(и):»')
            global PROOFS_FAILURE_TESTS
            PROOFS_FAILURE_TESTS = False

        if 'Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):' in each_file_in_folder:
            LOG.debug(
                '«Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):»')
            global AUTHORS_FAILURE_TESTS
            AUTHORS_FAILURE_TESTS = False

        if 'Ссылка(и) на источник(и):' in each_file_in_folder:
            LOG.debug(
                '«Ссылка(и) на источник(и):» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Ссылка(и) на источник(и):»')
            global LINK_FAILURE_TESTS
            LINK_FAILURE_TESTS = False

        if 'Постоянный адрес пакета:' in each_file_in_folder:
            LOG.debug(
                '«Постоянный адрес пакета:» contains in ' +
                filename_without_path)
        else:
            red_foreground(
                filename_without_path +
                ' not contains «Постоянный адрес пакета:»')
            global PACKAGE_LINK_FAILURE_TESTS
            PACKAGE_LINK_FAILURE_TESTS = False


def eric_head_summary():
    """Report, contains head data in all files or no."""
    eric_head_function()

    if all([DESCRIPTION_FAILURE_TESTS, TRAINING_PROCESS_FAILURE_TESTS, FIRST_EXAMPLE_FAILURE_TESTS,
            FIRST_ANSWER_FAILURE_TESTS, SECOND_EXAMPLE_FAILURE_TESTS, SECOND_ANSWER_FAILURE_TESTS,
            PROOFS_FAILURE_TESTS, AUTHORS_FAILURE_TESTS, LINK_FAILURE_TESTS, PACKAGE_LINK_FAILURE_TESTS]):
        global HEAD_DATA
        HEAD_DATA = True
        green_foreground(
            'All files contains correct head data')
    else:
        HEAD_DATA = False
        red_foreground('One or more packages not contains one or more head data. '
                       'Please, add correct head data to your package.')
