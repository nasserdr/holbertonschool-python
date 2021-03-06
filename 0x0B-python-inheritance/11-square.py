#!/usr/bin/python3
"""
Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The class square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializing the class
        """
        try:
            Rectangle.__init__(self, size, size)
            self.__size = size
            self.__size = size
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        """
        area
        """
        return self.__size*self.__size

    def __str__(self):
        """
        str
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
