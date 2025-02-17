# Charlotte Croce
# CSI 160
# Week 6: Lab - Loops
# 2/17/25

# 1. Area Codes
# Given a list of phone numbers that are missing the area code, 
# append the area code to the phone numbers in the list and return the result list.

def add_area_code(phone_numbers, area_code):
    """Returns a list of phone numbers with the area code added.
    Given a list of phone numbers that are missing the area code,
    append the area code to the phone numbers in the list and return the result list.

    :param phone_numbers: (list) A list of phone numbers (strings) that do not have the area code
                                Example: ['555-1212']
    :param area_code: (str) The area code to add Example: '802'
    :return: (list) A list of phone numbers with the area code Example: ['802-555-1212']
    """
    phone_numbers_with_area = phone_numbers.copy()
    for i in range(len(phone_numbers_with_area)):
        phone_numbers_with_area[i] = area_code + '-' + phone_numbers[i]
    return phone_numbers_with_area

# example usage
phone_numbers = ['555-1212', '999-0738']
with_area_code = add_area_code(phone_numbers, '802')
print(with_area_code)

################################################################
# 2. Print even numbers
# Complete the following function to print the even numbers of a list, one per line.

def print_even(numbers):
    """Prints the even numbers in a list, one per line

    :param numbers: (list) list of integers
    :return: None
    """
    for number in numbers:
        if number % 2 == 0:
            print(number)
 
print_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


################################################################
# 3. Guessing Game
# Extend your guessing game from earlier.  Write a program that picks a random number from 1-100.  Then ask the user to guess a number. 
# Tell the user if the answer is higher or lower than the number they guessed, or if they got the correct answer. 
# Allow them to guess again if they got the guess incorrect.  They should be able to guess numbers an infinite number 
# of times until they get the correct answer, at which point your loop will end.

# To generate a number from 1-100 you will need the following code at the beginning of your program:

from random import randint

def guessing_game():
    """Plays a guessing game where the user guesses a number between 1 and 100

    :return: None
    """
    randomNum = randint(1, 100)
    while True:
        guess = int(input("Guess a number 1-100: "))
        if guess < randomNum:
            print("Higher")
        elif guess > randomNum:
            print("Lower")
        else:
            print("Correct!")
            break

guessing_game()

################################################################
#4. Backpack of Stuff
#Complete the following code. Fill in the two sections of code identified in the comments.

import sys

def backpack_of_stuff():
    """Allows user to add and check items in a backpack

    :return: None
    """
    itemsInBackpack = ["book", "computer", "keys", "travel mug"]

    while True:
        print("Would you like to:")
        print("1. Add an item to the backpack?")
        print("2. Check if an item is in the backpack?")
        print("3. Quit")
        userChoice = input()
    
        if(userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()
            itemsInBackpack.append(itemToAdd)
        
        if(userChoice == "2"):   
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()
            if itemToCheck in itemsInBackpack:
                print("yes, this item is in backpack")
            else:
                print("no, this item is not in backpack")
    
        if(userChoice == "3"): 
            #sys.exit()
            break

backpack_of_stuff()

################################################################
# 5. Comma Code
# Say you have a list value like this:

# listToPrint = ['apples', 'bananas', 'tofu', 'cats']
#Write a program that prints a list with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, the above list would print 'apples, bananas, tofu, and cats'. 
# But your program should be able to work with any list not just the one shown above.
# Because of this, you will need to use a loop in case the list to print is shorter or longer than the above list. 
# Do not modify the list by inserting 'and' into the list and do not simply print the entire list 
# (you must loop through printing each item individually). This problem is trickier than it appears at first glance.

def comma_code(listToPrint):
    """Prints a list with all the items separated by a comma and a space, with 'and' inserted before the last item

    :param listToPrint: (list) A list of strings
    :return: None
    """
    
    # cases for list being 2, 1, or 0 elements
    if len(listToPrint) == 0:
        print("List is empty")
        return
    elif len(listToPrint) == 1:
        print(listToPrint[0])
        return
    elif len(listToPrint) == 2:
        print(listToPrint[0] + " and " + listToPrint[1])
        return
    
    else:
        for i in range(len(listToPrint) - 1): # loop through all but last element
            print(listToPrint[i], end=", ")
        print("and " + listToPrint[-1]) #print final element of list

comma_code(['apples', 'bananas', 'tofu', 'cats', 'dogs'])