
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

