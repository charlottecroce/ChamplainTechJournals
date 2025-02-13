def first_element(list_to_search):
    """Returns the first element of the supplied list.  Returns None if the list was empty"""
    if len(list_to_search) == 0:
        return None
    return list_to_search[0]


# Leave this part for easily testing your function
print('[4, 2, 15, 5] The first_element returns', first_element([4, 2, 15, 5]))
print('[] The first_element returns', first_element([]))
