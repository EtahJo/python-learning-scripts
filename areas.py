#!/usr/bin/env python3
import math


def perimeter(side1, side2, side3):
    """
    (number,number,number)-> float

    returns the perimeter of a triangle with sides side1, side2, side3

    >>> perimeter(3,4,5)
    12
    >>> perimeter(10.5,6,9.3)
    25.8
    """

    return side1 + side2 + side3


def semi_perimeter(side1, side2, side3):
    """
    (number,number,number)->float

    returns the semi perimeter of a triangle with sides side1, side2, side3

    >>> semi_perimeter(3,4,5)
    6.0
    >>> semi_perimeter(10.5,6,9.3)
    12.9
    """
    return perimeter(side1, side2, side3) / 2


def area_hero(side1, side2, side3):
    """
    (number,number,number)->float
    returns area of a triangle with sides of side1, side2, side3
    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5,6,9.3)
    27.73168

    """
    semi = semi_perimeter(side1, side2, side3)
    return math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))


print(area_hero(3, 4, 5))
print(area_hero(10.5, 6, 9.3))
