def is_legal_rook_move(initial_x, initial_y, final_x, final_y):
    """Returns True / False whether a given move is a legal move for the Rook.

    This function assumes that there are no other pieces on the board.

    :param initial_x: (int) Horizontal 1-8
    :param initial_y: (int) Vertical 1-8
    :param final_x:   (int) Horizontal 1-8
    :param final_y:   (int) Vertical 1-8
    :return: (bool) True / False if it is a legal move
    """
    # Complete this function
    return (initial_x != final_x) ^ (initial_y != final_y)

# Leave this part for easily testing your function
print('(4, 4, 5, 5) It is', is_legal_rook_move(4, 4, 5, 5), 'that this is a legal move')
print('(1, 4, 6, 4) It is', is_legal_rook_move(1, 4, 6, 4), 'that this is a legal move')
print('(1, 4, 1, 7) It is', is_legal_rook_move(1, 4, 1, 7), 'that this is a legal move')
