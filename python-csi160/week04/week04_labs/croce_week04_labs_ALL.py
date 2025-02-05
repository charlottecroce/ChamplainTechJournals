
#1. Implement a voting test. The user enters their age and then the program prints either,
# “You must be 18 to vote” or “You are of voting age”.

def voting_test():
    age = int(input("age: "))
    if age >= 18:
        print("You are of voting age")
    else:
        print("You must be 18 to vote")


voting_test()


#2. Ask the user to enter a grade percentage.  Convert the grade into a letter 
# grade using the official Champlain College grading scale.  For instance, if the user 
# types 99 then print A+.

def grade_to_letter():
    grade = int(input("GPA (100pt scale): "))
    if grade >= 97: letter = "A+"
    elif grade >= 93: letter = "A"
    elif grade >= 90: letter = "A-"
    elif grade >= 87: letter = "B+"
    elif grade >= 83: letter = "B"
    elif grade >= 80: letter = "B-"
    elif grade >= 77: letter = "C+"
    elif grade >= 73: letter = "C"
    elif grade >= 70: letter = "C-"
    elif grade >= 67: letter = "C+"
    elif grade >= 63: letter = "C"
    elif grade >= 60: letter = "C-"
    else: letter = "F"
    print(letter)


grade_to_letter()


# 3. Write a program that asks for two numbers. If the sum of the numbers is greater than 
# 100, print "They add up to a big number" if it is less than/equal to 100 than print "They add up to ____".

def add_to_big_number():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    sum = num1 + num2
    if sum > 100: 
        print("They add up to a big number")
    else:
        print("They add up to " + str(sum))


add_to_big_number()


#4. Implement a random number guessing game. The computer will pick a number at random from 
# 0-9, the user will be asked to guess the number.  Inform the user if they get the answer correct.

from random import randint

def random_number_game():
    num = randint(0,9)
    guess = int(input("random number guess(0-9): "))
    if guess == num:
        print("correct! you win")
    else:
        print("incorrect, the anser was", num)


random_number_game()


# 5. Write a function to compute whether a given year is a leap year in the Hebrew calendar.

def is_hebrew_leap_year(year):
    year_of_cycle = year % 19
    if year_of_cycle in (3, 6, 8, 11, 14, 17, 19):
        print(str(year) + " is year number " + str(year_of_cycle) + " of the cycle and is therefore a leap year.")
    else:
        print(str(year) + " is year number " + str(year_of_cycle) + " of the cycle and is therefore NOT a leap year.")


is_hebrew_leap_year(5779)
is_hebrew_leap_year(5780)
