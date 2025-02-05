def is_legal_king_move(initial_x, initial_y, final_x, final_y):
    """Returns True / False whether a given move is a legal move for the King.

    This function assumes that there are no other pieces on the board.

    :param initial_x: (int) Horizontal 1-8
    :param initial_y: (int) Vertical 1-8
    :param final_x:   (int) Horizontal 1-8
    :param final_y:   (int) Vertical 1-8
    :return: (bool) True / False if it is a legal move
    """
    # Complete this function

    if initial_x == final_x and initial_y == final_y:
        return False
    return abs(initial_x - final_x) <= 1 and abs(initial_y - final_y) <= 1




# Leave this part for easily testing your function
print('(4, 4, 5, 5) It is', is_legal_king_move(4, 4, 5, 5), 'that this is a legal move')
print('(1, 4, 6, 4) It is', is_legal_king_move(1, 4, 6, 4), 'that this is a legal move')
print('(1, 4, 1, 3) It is', is_legal_king_move(1, 4, 1, 3), 'that this is a legal move')
