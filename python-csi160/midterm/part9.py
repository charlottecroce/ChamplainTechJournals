'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a functon named 'above_main_diagonal' which receives a square matrix as parameter and returns the sum of the
elements above the main diagonal. The main diagonal is the one that goes from the top-left to the bottom-right of the
matrix. A number is characterized as above the main diagonal if its row index is less than its column index. The matrix
will always have at least one element.

Example:
matrix = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
print(above_main_diagonal(matrix))  # Output: 3. It will sum 1+1+1

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9,  10, 11, 12],
          [13, 14, 15, 16]]
print(above_main_diagonal(matrix))  # Output: 36. It will sum 2+3+4+7+8+12
'''
def above_main_diagonal(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row < col:
                sum += matrix[row][col]
    return sum


matrix = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
print(above_main_diagonal(matrix))  # Output: 3. It will sum 1+1+1

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9,  10, 11, 12],
          [13, 14, 15, 16]]
print(above_main_diagonal(matrix))  # Output: 36. It will sum 2+3+4+7+8+12