#!/usr/bin/python3
"""The introductory shabang line"""


class Rectangle:
    """The class Rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiating attributes.

        Args:
            width(int): The value of the width.
            height(int): The value of the height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            output = []
            for value in range(self.__height):
                [output.append('#') for value1 in range(self.__width)]
                if value != self.__height - 1:
                    output.append("\n")
            return ("".join(output))

    def __repr__(self):
        output = "Rectangle(" + str(self.__width)
        output += ", " + str(self.__height) + ")"
        return (output)

    def __del__(self):
        print("Bye rectangle...")
