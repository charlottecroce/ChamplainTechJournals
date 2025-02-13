def last_four_digits(phone_number):
    """ Returns the last 4 digits of a phone number as a string

    :param phone_number: (str) May be formatted "XXX-XXX-XXXX" or "1-XXX-XXX-XXXX"
    :return: (str) last four digits
    """
    return phone_number[-4:]


# Leave this part for easily testing your function
print('"802-555-1212"  last_four_digits returns', last_four_digits("802-555-1212"))
print('"1-410-617-3452"  last_four_digits returns', last_four_digits("410-617-3452"))
