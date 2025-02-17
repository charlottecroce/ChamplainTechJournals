def fibonacci(n):
    """Return the nth Fibonacci number. 

    param n: (int) position to determine fibonacci of
    return: (int) value at position n
    """
    
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers[n]

# Leave this part for easily testing your function
print('fibonacci(6) returns:', fibonacci(6), 'expected 8')
print('fibonacci(3) returns:', fibonacci(3), 'expected 2')
