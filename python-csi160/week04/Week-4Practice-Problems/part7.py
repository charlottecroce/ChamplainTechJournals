month = int(input('Enter the month: '))


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30")
else:
    print("28")

'''
month = month.lower()

if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    print("31")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print("30")
else:
    print("28")
'''