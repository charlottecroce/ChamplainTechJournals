def num_distinct_elements(numbers):
    """Determine the number of distinct elements in the list

    :param numbers: (list) A list of numbers (int or float)
    :return: (int) Number of distinct elements
    """
    # Use the function sorted() to temporarily sort the numbers
    # into ascending order or use the method .sort() to permanently
    # sort the list in ascending order.
    numbers.sort()
    unique_numbers = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            unique_numbers += 1
    return unique_numbers




# Leave this part for easily testing your function
test1 = [2, 5, 5, 7,2, 9.5, 2, 4]
print(f'num_distinct_elements({test1}) returns:', num_distinct_elements(test1))
test2 = [2, 1, 1, 7, 1, 9.5, 2, 1]
print(f'num_distinct_elements({test2}) returns:', num_distinct_elements(test2))

