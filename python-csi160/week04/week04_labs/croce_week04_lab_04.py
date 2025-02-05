
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

