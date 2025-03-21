import pickle
import sys
import pwnedpasswords
import random
import string

# The password list - We start with it populated for testing purposes
entries = {'yahoo': {'username': 'johndoe', 'password': 'cus#u%S tu', 'url': 'https://www.yahoo.com'},
           'google': {'username': 'johndoe', 'password': '`q$$( #tABCD^ %fu#*W  t', 'url': 'https://www.google.com'}}

# The password file name to store the data to
password_file_name = "PasswordFile.pickle"

# The encryption key for the caesar cypher
encryption_key = 16

menu_text = """
What would you like to do:
1. Open password file
2. Add an entry
3. Lookup an entry
4. Save password file
5. Quit program
6. Print dictionary for testing
7. Delete an entry
8. Edit an entry
Please enter a number (1-8)"""

def password_encrypt(unencrypted_message, key):
    """Returns an encrypted message using a caesar cypher
    :param unencryptedMessage (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    """
    result_string = ''
    min_limit = 32
    max_limit = 126
    for character in unencrypted_message:
        value = ord(character) - min_limit + key
        value = value % (max_limit - min_limit + 1)
        value = value + min_limit
        result_string = result_string + chr(value)
    return result_string

def password_decrypt(encrypted_message, key):
    """Returns a decrypted message.
    :param encrypted_message (string):
    :param key (int) The offset that was used to encrypt the message
    :return (string): The decrypted message
    """
    return password_encrypt(encrypted_message, -key)

def load_password_file():
    """Loads a password file.  The file must be in the same directory as the .py file
    """
    global entries, encryption_key
    try:
        entries, encryption_key = pickle.load(open(password_file_name, "rb"))
        print(f"Password file '{password_file_name}' loaded successfully!")
    except FileNotFoundError:
        print(f"File '{password_file_name}' not found. Starting with an empty dictionary.")
        entries = {}
    except Exception as e:
        print(f"Error loading file: {e}")

def save_password_file():
    """Saves a password file.  The file will be created if it doesn't exist.
    """
    try:
        pickle.dump((entries, encryption_key), open(password_file_name, "wb"))
        print(f"Password file '{password_file_name}' saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def generate_random_password(length=12):
    """Generates a random password that meets complexity requirements.
    
    The generated password will:
    - Be at least 8 characters long (default 12)
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one digit
    - Contain at least one special character
    
    :param length (int): Length of the password to generate (minimum 8)
    :return (string): A randomly generated password meeting all requirements
    """
    if length < 8:
        length = 8  # Enforce minimum length
    
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    # Ensure we have at least one of each required character type
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest with random characters from all allowed sets
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password characters to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

def check_password_complexity(password):
    """Checks if a password meets complexity requirements.
    
    Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    :param password (string): The password to check
    :return (tuple): (bool, string) - True if the password meets all requirements, 
                    False otherwise, and a message explaining the result
    """
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    
    # Check for digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    
    # Check for special character
    special_chars = "!@#$%^&*()-_+=<>?/[]{}|\\~`"
    if not any(char in special_chars for char in password):
        return False, "Password must contain at least one special character."
    
    return True, "Password meets all complexity requirements."

def add_entry():
    """Adds an entry with an entry title, username, password and url
    Includes all user interface interactions to get the necessary information from the user
    """
    try:
        entry_title = input("Enter entry title: ")
        username = input("Enter username: ")
        
        # Explain password requirements
        print("\nPassword requirements:")
        print("- At least 8 characters long")
        print("- Contains at least one uppercase letter")
        print("- Contains at least one lowercase letter")
        print("- Contains at least one digit")
        print("- Contains at least one special character (!@#$%^&*()-_+=<>?/[]{}|\\~`)\n")
        
        # Ask if user wants to generate a random password
        gen_password = input("Would you like to generate a random password? (y/n): ")
        
        if gen_password.lower() == 'y':
            # Ask for desired password length
            try:
                length = int(input("Enter desired password length (minimum 8, default 12): ") or "12")
                if length < 8:
                    print("Password length must be at least 8. Setting to 8.")
                    length = 8
            except ValueError:
                print("Invalid input. Using default length of 12.")
                length = 12
                
            # Generate the password
            password = generate_random_password(length)
            print(f"Generated password: {password}")
            is_valid = True
        else:
            # Get and validate manual password
            print("Enter your password manually:")
            while True:
                password = input("Enter password: ")
                is_valid, message = check_password_complexity(password)
                if is_valid:
                    print(message)
                    break
                else:
                    print(message)
                    print("Please try again with a stronger password.")
        
        url = input("Enter URL: ")
        
        # Encrypt the password
        encrypted_password = password_encrypt(password, encryption_key)
        
        # Add the new entry to the entries dictionary
        entries[entry_title] = {
            'username': username,
            'password': encrypted_password,
            'url': url
        }
        
        print(f"Entry '{entry_title}' added successfully!")
    except Exception as e:
        print(f"Error adding entry: {e}")

def print_entry():
    """Asks the user for the name of the entry and prints all related information in a pretty format. 
    Includes all information about an entry.
    """
    try:
        print("Which entry do you want to lookup the information for?")
        for key in entries:
            print(key)
        
        entry = input('Enter entry name: ')
        
        # Check if the entry exists
        if entry in entries:
            entry_data = entries[entry]
            
            # Decrypt the password
            decrypted_password = password_decrypt(entry_data['password'], encryption_key)
            
            # Print the entry information
            print("\n--- Entry Information ---")
            print(f"Entry: {entry}")
            print(f"Username: {entry_data['username']}")
            print(f"Password: {decrypted_password}")
            print(f"URL: {entry_data['url']}")
            print("------------------------\n")
        else:
            print(f"Entry '{entry}' not found!")
    except KeyError:
        print(f"Error: The entry does not exist or has incomplete data.")
    except Exception as e:
        print(f"Error looking up entry: {e}")

def delete_entry():
    """Deletes an entry from the password manager.
    Asks the user for the entry name to delete and removes it if it exists.
    
    This is additional feature #1.
    """
    try:
        print("Which entry do you want to delete?")
        for key in entries:
            print(key)
        
        entry = input('Enter entry name: ')
        
        # Check if the entry exists
        if entry in entries:
            # Ask for confirmation
            confirm = input(f"Are you sure you want to delete '{entry}'? (y/n): ")
            if confirm.lower() == 'y':
                # Remove the entry
                del entries[entry]
                print(f"Entry '{entry}' deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Entry '{entry}' not found!")
    except Exception as e:
        print(f"Error deleting entry: {e}")

def edit_entry():
    """Allows the user to edit an existing entry in the password manager.
    The user can update the username, password, and/or URL.
    
    This is additional feature #2.
    """
    try:
        print("Which entry do you want to edit?")
        for key in entries:
            print(key)
        
        entry = input('Enter entry name: ')
        
        # Check if the entry exists
        if entry in entries:
            entry_data = entries[entry]
            print(f"\nEditing entry: {entry}")
            
            # Get current values for reference
            current_username = entry_data['username']
            current_url = entry_data['url']
            
            # Update username
            new_username = input(f"Enter new username (current: {current_username}) or press Enter to keep current: ")
            if new_username:
                entry_data['username'] = new_username
            
            # Update password
            update_password = input("Do you want to update the password? (y/n): ")
            if update_password.lower() == 'y':
                # Explain password requirements
                print("\nPassword requirements:")
                print("- At least 8 characters long")
                print("- Contains at least one uppercase letter")
                print("- Contains at least one lowercase letter")
                print("- Contains at least one digit")
                print("- Contains at least one special character (!@#$%^&*()-_+=<>?/[]{}|\\~`)\n")
                
                # Ask if user wants to generate a random password
                gen_password = input("Would you like to generate a random password? (y/n): ")
                
                if gen_password.lower() == 'y':
                    # Ask for desired password length
                    try:
                        length = int(input("Enter desired password length (minimum 8, default 12): ") or "12")
                        if length < 8:
                            print("Password length must be at least 8. Setting to 8.")
                            length = 8
                    except ValueError:
                        print("Invalid input. Using default length of 12.")
                        length = 12
                        
                    # Generate the password
                    new_password = generate_random_password(length)
                    print(f"Generated password: {new_password}")
                    
                    # Encrypt the new password
                    entry_data['password'] = password_encrypt(new_password, encryption_key)
                else:
                    # Get and validate new password manually
                    while True:
                        new_password = input("Enter new password: ")
                        is_valid, message = check_password_complexity(new_password)
                        if is_valid:
                            print(message)
                            # Encrypt the new password
                            entry_data['password'] = password_encrypt(new_password, encryption_key)
                            break
                        else:
                            print(message)
                            print("Please try again with a stronger password.")
            
            # Update URL
            new_url = input(f"Enter new URL (current: {current_url}) or press Enter to keep current: ")
            if new_url:
                entry_data['url'] = new_url
            
            print(f"Entry '{entry}' updated successfully!")
        else:
            print(f"Entry '{entry}' not found!")
    except Exception as e:
        print(f"Error editing entry: {e}")

def end_program():
    """Exits the program.
    """
    sys.exit()

def print_dictionary():
    """Prints the current entries dictionary.
    For testing purposes only.
    """
    print(entries)

# Menu dictionary mapping user choices to functions
menu_dict = {'1': load_password_file,
             '2': add_entry,
             '3': print_entry,
             '4': save_password_file,
             '5': end_program,
             '6': print_dictionary,
             '7': delete_entry,
             '8': edit_entry}

# Main program loop
while True:
    try:
        user_choice = input(menu_text)
        if user_choice in menu_dict and menu_dict[user_choice]:
            menu_dict[user_choice]()
        else:
            print('Not a valid choice')
    except Exception as e:
        print(f"An error occurred: {e}")