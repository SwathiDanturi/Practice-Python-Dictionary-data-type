"""
Practice with the dictionary built-in data type.

File: client.py
Initial developers: COMP 801 instructors
Developer: Swathi
Collaborator(s): Ruchitha
Date: 10/03/2024
"""
from programming_languages import ProgrammingLanguages


def main():
    """
    Demo ProgrammingLanguages functionality
    """
    programmers = ['Bill', 'Joan']
    # `courses` must be parallel with `days`
    languages = [['C++', 'Python'], ['C++']]

    language_obj = ProgrammingLanguages(
        programmers, languages)

    print(language_obj.find_languages("Bill"))  # ['C++', 'Python']
    print(language_obj.find_programmers("C++"))  # ["Bill", "Joan"]


if __name__ == "__main__":
    main()
