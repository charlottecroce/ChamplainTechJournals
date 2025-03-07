'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a function named exactly 'divide_and_remainder' and receive a parameter 'num' and a base 'b' and returns a tuple
where: he first element is the result of integer division, and the second element is the remainder.

Example:
print(divide_and_remainder(10, 3))  # Output: (3, 1)
print(divide_and_remainder(10, 2))  # Output: (5, 0)
'''

def divide_and_remainder(num, b):
    return (num // b, num % b)

print(divide_and_remainder(10, 3))  # Output: (3, 1)
print(divide_and_remainder(10, 2))  # Output: (5, 0)