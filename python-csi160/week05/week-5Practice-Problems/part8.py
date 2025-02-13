def area_code(phone_number):
    """Returns the area code of the supplied phone number.

    params:
        phone_number (string) in the format:
            1-XXX-XXX-XXXX
            XXX-XXX-XXXX
            (XXX)-XXX-XXXX
    return: (string) The area code
    """
    if phone_number[0] == '(':
        return phone_number[1:4]
    elif phone_number[0] == '1':
        return phone_number[2:5]
    else:
        return phone_number[:3]




# Leave this part for easily testing your function
print('"1-617-555-1212" area_code returns', area_code("1-617-555-1212"))
print('"802-999-1212" area_code returns', area_code("802-999-1212"))
print('"(802)-999-1212" area_code returns', area_code("(802)-999-1212"))
