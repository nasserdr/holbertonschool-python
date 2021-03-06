#!/usr/bin/python3
"""
 class to define a rectange
"""


class Rectangle:
    """
    defines the square class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initializes the classe rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        The getter"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        The getter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the setter of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle:
        """
        return self.__width*self.__height

    def perimeter(self):
        """
        Returns the perimieter of the rectangle
        """
        return 2*(self.__width + self.__height)

    def __str__(self):
        """
        prints the string representation of the rect
        """
        s = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                s += str(self.print_symbol)
            s += "\n"
        return s[:-1]

    def __repr__(self):
        """
        defines the repr of the object
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Upon instance deletion
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1

    def bigger_or_equal(rect_1, rect_2):
        """
        compare 2 rectangles
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """
        return a new instance with width = height
        """
        return Rectangle(size, size)
