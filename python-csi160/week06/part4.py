def introductions(names):
    """Prints introductions.

    An introduction is 'Hello' followed by a space and a name.
    Include a newline after each introduction.
    Example:
    'Hello Josh'

    Important: Your function should use print() and not have a return statement

    :param names: (list) First Names as strings
    :return: None
    """
    for name in names:
        print("Hello", name)


# Leave this part for easily testing your function
sample_names = input('Enter the names separated by a comma and a space: ').split(', ')
introductions(sample_names)

