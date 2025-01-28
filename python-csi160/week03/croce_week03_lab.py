"""

Author: Charlotte Croce
Class: CSI 160
Assignment: Week 3 Lab
Due Date: 2/3/25

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

from math import pi


def fahrenheit_to_celcius(temperature_in_fahrenheit):
    """This function converts a number from Fahrenheit to Celcius

    :param temperature_in_fahrenheit (float): The temperature to convert

    :return (float): The temperature in Fahrenheit

    Assumptions: temperature_in_fahrenheit is a float

    """
    try:
        return round(((temperature_in_fahrenheit - 32) * 5 / 9), 2)
    except TypeError:
        print("invalid input: input floats please")
        return  

celcius_temp = float(input("---\n1. temp in fahrenheit: "))
print("1. coverted to celcius:", fahrenheit_to_celcius(celcius_temp))


def cylinder_volume(radius, height):
    """Computes volume of a cylinder

    :param radius: positive float

    :param height: positive float

    :return: volume of cylinder
            
    Assumptions: inputs are floats
    """
    try:
        return round((pi * (radius*radius) * height), 2)
    except TypeError:
        print("invalid input: input floats please")
        return

cylinder_radius = float(input("---\n2. cylinder radius: "))
cylinder_height = float(input("2. cylinder height: "))
print("2. cylinder volume:", cylinder_volume(cylinder_radius, cylinder_height))


def surface_area_rectangular_prism(length, width, height):
    """Computes surface area of a rectangular prism

    :param length: positive float

    :param width: positive float

    :param height: positive float

    :return: surface area of a rectangular prism

    Assumptions: inputs are floats
    """
    try:
        return round((2 * ((length*width)+(length*height)+(width*height))), 2)
    except TypeError:
        print("invalid input: input floats please")
        return
    
rectangular_prism_length = float(input("---\n3. rectangular prism length: "))
rectangular_prism_width = float(input("3. rectangular prism width: "))
rectangular_prism_height = float(input("3. rectangular prism height: "))
print("3. rectangular prism surface area:", surface_area_rectangular_prism(rectangular_prism_length,rectangular_prism_width,rectangular_prism_height))

