# Statement

Given a month - an integer from 1 to 12, print the number of days in it assuming a non-leap year.

Hint: 'or' statements can make this much easier, but be careful when setting up 'or' statements:

```
# This is correct!
if age == 5 or age == 6:   

# This is WRONG because of order of operations 
# '==' has precedence over 'or', since 6 evaluates to True
# this will ALWAYS be True
if age == 5 or 6: 
```
The Gregorian calendar consists of the following 12 months:

1. January - 31 days
2. February - 28 days in a non-leap year
3. March - 31 days
4. April - 30 days
5. May - 31 days
6. June - 30 days
7. July - 31 days
8. August - 31 days
9. September - 30 days
10. October - 31 days
11. November - 30 days
12. December - 31 days

# Example input #1

```
1
```

(January)

# Example output #1

```
31
```

# Example input #2

```
2
```

(February)

# Example output #2

```
28
```

