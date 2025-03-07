'''
Do not use AI! You can schedule to try again if you have a bad grade!
This is a bonus question, and it might hard. It is not mandatory to solve it. You can skip it if you want.
Spiral Matrix is a matrix of size 'n x n' filled with numbers from 1 to (n*n) in a spiral order.
Write a function 'spiral_matrix' that receives an integer 'n' as parameter and returns a list of lists representing the spiral matrix.
Examples of Spiral Matrix:
n = 1
[[1]]
n = 2
[[1, 2],
 [4, 3]]
n = 3
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]
n = 4
[[1,  2,  3,  4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9,  8,  7]]

Example:
print(spiral_matrix(3))
# Output:
[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
'''

def spiral_matrix(n):
    # create an empty n x n matrix filled with zeros
    matrix = [[0 for i in range(n)] for j in range(n)]

    counter = 1
    row = 0
    col = 0
    
    for i in range(1, n*n):
        while col < n - i:
            matrix[row][col] = counter
            counter += 1
            col += 1

        while row < n - i:            
            matrix[row][col] = counter
            counter += 1
            row += 1

        while col > 0 + (i - 1):
            matrix[row][col] = counter
            counter += 1
            col -= 1

        while row > 0 + i:
            matrix[row][col] = counter
            counter += 1
            row -= 1
    
    matrix[row][col] = counter
    return matrix

print(spiral_matrix(5))
# Output:
[[1, 2, 3], [8, 9, 4], [7, 6, 5]]