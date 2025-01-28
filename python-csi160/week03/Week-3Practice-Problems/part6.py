from math import pi  # This lets you refer to pi in your code


def volume_cone(radius, height):
    """Computes volume of a cone

    :param radius: positive float

    :param height: positive float

    :return: volume of given cone
    """
    return 1/3 * pi * (radius*radius) * height