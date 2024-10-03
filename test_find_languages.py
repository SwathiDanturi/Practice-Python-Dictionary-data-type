"""
Practice with the dictionary built-in data type.

File: test_find_languages.py
Initial developers: COMP 801 instructors
Developer: Swathi
Collaborator(s): Ruchitha
Date: 10/03/2024
"""

from programming_languages import ProgrammingLanguages


def test_find_langauges_2_2_1():
    """
    Test constructor with two programmers, 1st with 2 programming langauges,
    2nd programmer with 1 programmin glangauge
    """
    programmers = ["Bill", "Joan"]
    languages = [["C++", "Python"], ["C++"]]

    language_obj = ProgrammingLanguages(programmers, languages)

    expected = ["C++", "Python"]
    actual = language_obj.find_languages("Bill")

    assert expected == actual
