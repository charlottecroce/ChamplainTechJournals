def last_element(list_to_search):
    """Returns the last element of the supplied list.
    Returns None if the list is empty"""
    if len(list_to_search) == 0:
        return None
    return list_to_search[-1]


# Leave this part for easily testing your function
print('[4, 2, 15, 5] The last_element returns', last_element([4, 2, 15, 5]))
print('[] The last_element returns', last_element([]))
