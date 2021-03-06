#!/usr/bin/python3
"""
Checks if a class inherits from another class
"""


def inherits_from(obj, a_class):
    """
    Return true if obj inerits from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
