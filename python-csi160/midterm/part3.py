'''
Do not use AI! You can schedule to try again if you have a bad grade!
This question can be challenging, so leave it to the end if you are running out of time.
Lucas Sequence Write a function 'lucas' which receives an integer 'n' as parameter and returns the 'n-th' element of the
 lucas sequence. The Lucas sequence is a series of numbers in which each number is the sum of the two preceding just
 like fibonacci, but the first two numbers are 2 and 1, instead of 0 and 1. So the sequence goes like this:
 2, 1, 3, 4, 7, 11, 18, 29...

Do not use recursion to solve this problem.

Examples:
lucas(0)  # returns 2
lucas(1)  # returns 1
lucas(2)  # returns 3
lucas(5)  # returns 11
'''
def lucas(n):
    lucas_numbers = [2, 1]
    for i in range(2, n + 1):
        lucas_numbers.append(lucas_numbers[i - 1] + lucas_numbers[i - 2])
    return lucas_numbers[n]

print(lucas(0))  # returns 2
print(lucas(1))  # returns 1
print(lucas(2))  # returns 3
print(lucas(5))  # returns 11