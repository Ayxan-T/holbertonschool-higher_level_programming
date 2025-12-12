#!/usr/bin/python3
"""
    a module with a Rectangle class
"""


class Rectangle:
    """
        a Rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def bigger_or_equal(rect_1, rect_2):
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.perimeter() == 0:
            return ""
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                res = res + str(self.print_symbol)
            if i < self.height - 1:
                res = res + "\n"
        return res

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2*self.height + 2*self.width
