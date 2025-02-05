
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

