"""
Author: Charlotte Croce
Class: CSI160
Assignment: Week 2: Lab - Conversation with a Computer
Due Date: 1/27/25

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


"""
Write a program that has a conversation with the user. The program must ask for strings, integers and floats as input. 
The program must ask for at least 4 different inputs from the user. The program must reuse atleast 4 of these inputs in what it displays on the screen. 
The program must perform at least 2 arithmetic operations on the numbers the user inputs.  Please turn in your .py file.
"""

print("hello! i am a robot. beep beep")
# ask for name
name = input("what is your name?")
# say hi and ask for favorite color
favorite_color = input("hello " + name + ", what is your favorite color?")
# ask if user likes ice cream
user_likes_icecream = input("mine too, do you like Ice Cream?")
# answer differently based on whether user answers 'yes' or not
if(user_likes_icecream.lower() == "yes"):
    print("me too!")
else:
    print("okay, not for everyone")
# ask for age
age = int(input(name + ", how old are you?"))
# ask for number of siblings
siblings = int(input("...and how many siblings do you have?"))
# display how many kids you a part of; ask if favorite color is shared by anyone in the house
is_favorite_color_of_house = input("that means you are one of " + str(siblings + 1) + " kid(s). is " + favorite_color + " the favorite color of anyone else in your house?")
# answer differently based on whether user answers 'yes' or not
if(is_favorite_color_of_house.lower() == "yes"):
    print("good you can agree")
else:
    print("too bad")
# ask for parent's age
parent_age = int(input('how old is one of your parents?'))
# respond with age of parents when they had the user
print("that means they were likely " + str(parent_age - age) + " when they had you")
# ask for GPA
gpa = float(input("what is your GPA[4-point scale]?"))
# answer differently based on the GPA value entered
if(gpa >= 3.5):
    print("great job!")
elif(gpa >= 2.5):
    print("keep it up!")
else:
    print("time to study more!")
print("goodbye!")
