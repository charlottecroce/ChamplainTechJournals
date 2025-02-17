def all_squares(n):
    """Returns a list that contains all the squares of positive integers
    where the square is less than or equal to N, in ascending order.

    :param n: (int) Upper bound
    :return: (list) List of squares
    """
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    return squares


# Leave this part for easily testing your function
print('all_squares(50) returns:', all_squares(50))
print('all_squares(9) returns:', all_squares(9))
