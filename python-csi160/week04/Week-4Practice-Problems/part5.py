def one_positive(num1, num2):
    """Given two non-zero integers, returns True if exactly one of
    them is positive and returns False otherwise.

    :param num1: non-zero integer
    :param num2: non-zero integer
    :return: True / False
    """
    # Complete this function
    return (num1 > 0) ^ (num2 > 0)


# Leave this part for easily testing your function
print('(5, 7) It is', one_positive(5, 7), 'that only one of these numbers is positive')
print('(-5, -7) It is', one_positive(-5, -7), 'that only one of these numbers is positive')
print('(5, -7) It is', one_positive(5, -7), 'that only one of these numbers is positive')