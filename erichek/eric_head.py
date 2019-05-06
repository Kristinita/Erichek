# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-26 10:06:04
# @Last Modified time: 2019-05-04 09:10:16
"""Check files for correct head metadata.

Check, that files contains «Описание пакета:», «Процесс тренировки:» and so on.
"""
from erichek.eric_config import eric_opened_files
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_error


def eric_head(head_metadata):
    """Check, that files contains metadata.

    Wrapper, contains certain metadata in files or no.
    Lists and generators differences:
    https://www.severcart.org/blog/all/understanding_yield_in_Python/

    Arguments:
        head_metadata {str} -- metadata of Erichek rooms string

    Yields:
        bool -- return False, if any error in any file

    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_pylint, pylint_as_string in eric_opened_files():
        if head_metadata in pylint_as_string:
            pyfancy_debug(f"{filename_pylint}: “{head_metadata}” exists")
        else:
            pyfancy_error(f"{filename_pylint}: “{head_metadata}” not exists. "
                          f"Please, add “{head_metadata}” to {filename_pylint}.")
            yield False


def eric_package_description():
    """Check «Описание пакета:».

    Python >= 3.3, PEP 380: yield from is equivalent:
    for item in iterable:
        yield item
    https://pythonworld.ru/novosti-mira-python/chto-novogo-v-python-33.html

    yield always return generator:
    https://stackoverflow.com/a/25313357/5951529
    """
    yield from eric_head('Описание пакета:')


def eric_proof():
    """Check «Источник(и):»."""
    yield from eric_head('Источник(и):')


def eric_authors_and_editors():
    """Check «Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):»."""
    yield from eric_head(
        'Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):')


def eric_prooflink():
    """Check «Ссылка(и) на источник(и):»."""
    yield from eric_head('Ссылка(и) на источник(и):')
