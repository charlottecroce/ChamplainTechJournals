'''
Do not use AI! You can schedule to try again if you have a bad grade!
Write a function named 'split_full_name' which receives a parameter 'full_name' with 2 or more surnames and returns a
tuple with the last name and the first name. The full name will be a string with the following format:
"first_name middle1 middle2 ... lastname" where middle1, middle2, ... are optional middle names and the last word is the
 last name. The function should return a tuple with the last name and the first name. If the full name has only one
 word, the function should return a tuple with the word as the last name and an empty string as the first name.

Example:
print(split_full_name("John Doe"))  # Output: ('Doe', 'John')
print(split_full_name("John Doe Smith"))  # Output: ('Smith', 'John')
print(split_full_name("John"))  # Output: ('John', '')
print(split_full_name("John Doe Smith Lee"))  # Output: ('Lee', 'John')
'''
def split_full_name(full_name):
    namelist = full_name.split(" ")
    if len(namelist) < 2:
        return (namelist[0], '')
    return (namelist[-1], namelist[0])

print(split_full_name("John Doe"))  # Output: ('Doe', 'John')
print(split_full_name("John Doe Smith"))  # Output: ('Smith', 'John')
print(split_full_name("John"))  # Output: ('John', '')
print(split_full_name("John Doe Smith Lee"))  # Output: ('Lee', 'John')