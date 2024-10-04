"""
Practice with the dictionary built-in data type.

File: test_find_programmers.py
Initial developers: COMP 801 instructors
Developer: Swathi
Collaborator(s): Ruchitha
Date: 10/03/2024
"""

import pytest
from programming_languages import ProgrammingLanguages


def test_find_programmers_one_programmer():
    """
    Test find_programmers with one programmer
    proficient in the given input language
    """
    programmers = ['Bill', 'Joan']
    languages = [['C++', 'Python'], ['C++']]
    pl_obj = ProgrammingLanguages(programmers, languages)
    expected = ['Bill']
    actual = pl_obj.find_programmers('Python')
    assert actual == expected


def test_find_programmers_more_than_one_programmer():
    """
    Test find_programmers with more than one programmer
    proficient in the given input language
    """
    programmers = ['Bill', 'Joan']
    languages = [['C++', 'Python'], ['C++']]
    pl_obj = ProgrammingLanguages(programmers, languages)
    expected = ['Bill', 'Joan']
    actual = pl_obj.find_programmers('C++')
    assert actual == expected


pytest.main()
