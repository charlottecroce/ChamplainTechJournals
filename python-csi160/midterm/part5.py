'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a function named exactly "median" which receives a list of element as parameter and returns the median value of
the list. The median is the value separating the higher half from the lower half of a data sample. If the list has an
even number of elements, the function should return the average of the two middle elements. You should not modify the
original list, but you can sort in a copy of the list.

Example:
median([1, 2, 3, 4, 5])     # returns: 3
median([1, 2, 3, 4, 5, 6])  # returns: 3.5
'''
def median(numbers):
    sortedNums = sorted(numbers)
    length = len(sortedNums)
    mid = length // 2
    if length % 2 == 0: # even number-> avg of middle two
        return (sortedNums[mid - 1] + sortedNums[mid]) / 2
    else: # odd number-> middle element
        return sortedNums[mid]

print(median([1, 3, 2, 4, 5]))     # returns: 3
print(median([1, 2, 3, 4, 5, 6]))  # returns: 3.5