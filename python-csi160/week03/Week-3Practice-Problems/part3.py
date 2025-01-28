# Read an integer:
number = int(input('Enter a 3 digit number: '))

# Print the sum of the digits:

a = ((number // 100) + (number % 100 // 10) + (number % 10))
print(a)
