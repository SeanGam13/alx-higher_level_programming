#!/usr/bin/python3
"""A module that contains a Rectangle class"""


class Rectangle:
    """defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """get the width of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print output of the rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """The internal representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """method called when del keyword is used"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
