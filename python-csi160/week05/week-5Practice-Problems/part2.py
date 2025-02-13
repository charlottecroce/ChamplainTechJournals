def second_element(list_to_search):
    """Returns the second element of the supplied list.  Returns None if list contains less than 2 elements"""
    if len(list_to_search) < 2:
        return None
    return list_to_search[1]


# Leave this part for easily testing your function
print('[4, 2, 15, 5] The second_element returns', second_element([4, 2, 15, 5]))
print('[3] The second_element returns', second_element([3]))
