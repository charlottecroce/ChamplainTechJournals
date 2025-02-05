
#1. Implement a voting test. The user enters their age and then the program prints either,
# “You must be 18 to vote” or “You are of voting age”.

def voting_test():
    age = int(input("age: "))
    if age >= 18:
        print("You are of voting age")
    else:
        print("You must be 18 to vote")


voting_test()

