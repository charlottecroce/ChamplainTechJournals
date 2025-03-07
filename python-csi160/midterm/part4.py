'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a function named exactly "last2" which receives a list of elements as parameter and then return the second element
 from the end to the beginning of the list. If the list has less than two elements, the function should return None.

Example:
print(last2(['red', 'blue', 'green', 'yellow']))  # Output: green
print(last2([0,1]))  # Output: 0
print(last2([0]))  # Output: None
'''
def last2(lst):
    if len(lst) < 2:
        return None
    else:
        return lst[-2]

print(last2(['red', 'blue', 'green', 'yellow']))  # Output: green
print(last2([0,1]))  # Output: 0
print(last2([0]))  # Output: None