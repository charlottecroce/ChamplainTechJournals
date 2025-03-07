'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a function named 'countdown' which receives a parameter 'n' and returns a list with the countdown from 'n' to 0
both included. If 'n' is less than 0, the function should return an empty list.

Example:
print(countdown(5))  # Output: [5, 4, 3, 2, 1, 0]
print(countdown(0))  # Output: [0]
print(countdown(-1))  # Output: []
print(countdown(10))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''
def countdown(n):
    lst = []
    for i in range(n, -1, -1):
        lst.append(i)
    return lst

print(countdown(5))  # Output: [5, 4, 3, 2, 1, 0]
print(countdown(0))  # Output: [0]
print(countdown(-1))  # Output: []
print(countdown(10))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]