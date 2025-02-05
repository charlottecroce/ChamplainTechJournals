def ascending_digits(num):
    """Given a three-digit integer X consisting of three different digits,
    returns True if its three digits are going in an ascending
    order from left to right and returns False otherwise.

    :param num: three digit integer
    :return: True / False
    """
    # Complete this function
    # Hint: assign variables for each digit first
    # then build the comparison

    a = num // 100
    b = num % 100 // 10
    c = num % 10
    
    ascending=False
    if a < b and b < c:
        ascending = True

    return ascending


# Leave this part for easily testing your function
print('(136) It is', ascending_digits(136), 'that the digits are ascending')
print('(462) It is', ascending_digits(462), 'that the digits are ascending')
print('(823) It is', ascending_digits(823), 'that the digits are ascending')