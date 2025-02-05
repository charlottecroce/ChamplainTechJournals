
# 5. Write a function to compute whether a given year is a leap year in the Hebrew calendar.

def is_hebrew_leap_year(year):
    year_of_cycle = year % 19
    if year_of_cycle in (3, 6, 8, 11, 14, 17, 19):
        print(str(year) + " is year number " + str(year_of_cycle) + " of the cycle and is therefore a leap year.")
    else:
        print(str(year) + " is year number " + str(year_of_cycle) + " of the cycle and is therefore NOT a leap year.")


is_hebrew_leap_year(5779)
is_hebrew_leap_year(5780)
