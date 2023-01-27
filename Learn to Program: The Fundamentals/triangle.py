import math

def area(base, height):
    '''(number, number) -> number

    Return the area of a triangle with dimensions base and height.

    >>> area(10,5)
    25.0
    >>>area(2.5, 3)
    3.75
    '''
    
    return base * height / 2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of a triangle with sides of lenght side1, side2 and side3.

    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 15, 20.2)
    45.7
    '''
    
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the simeprimeter of a tringle with sides of lenght side1, side2 and side3.

    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 15, 20.2)
    12.9
    '''

    return perimeter(side1, side2, side3) / 2

def area_hero(side1, side2, side3):
    '''(number, number, number) -> float

    Return the area of a triangle with sides of lenght side1, side2 and side3.

    >>> area_hero(3, 4, 5)
    6.0
    >>> area_hero(10.5, 6, 9.3)
    27.73168584850189
    '''

    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area

