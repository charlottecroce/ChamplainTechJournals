
# Step 1. Create dictionary called 'user'
# with the following keys: 'name' and 'location'
# Set the name to 'John Doe'
# Set the location to 'Burlington, VT'

user = {
    'name': 'John Doe',
    'location': 'Burlington, VT'
}

# Step 2. Ask the user for the user's age
# and create a key/value pair in user to store this
# called 'age'
try:
    age = input(f"How old is {user['name']}? ")
except KeyError:
    print('"name" not defined as a key in Step 1')
else:
    user['age'] = int(age)
    print(f"{user['name']} is {user['age']} years old.")
  

# Step 3
# Create keys "first_name" and "last_name"
# Use .split() to seperate name into firstname and last_name
# Remove the key "name" from the dictionary

first_name, last_name = user['name'].split()
user['first_name'] = first_name
user['last_name'] = last_name
del user['name']
print(f"First name: {user['first_name']}")
print(f"Last name: {user['last_name']}")


# For testing (do not delete)
print('Printing "user":')
print(user)
