"""
Do not use AI! You can schedule to try again if you have a bad grade!
Basic Function Write a function named exactly "calculate_discounted_price" which receives 2 parameters: price(float)
and discount(float) in percentage, and returns the final price after applying the discount.

Example:
print(calculate_discounted_price(100, 10))  # Output: 90.0
print(calculate_discounted_price(50, 50))  # Output: 25.0
"""
def calculate_discounted_price(price, discount):
    return price - (price * discount * .01)

print(calculate_discounted_price(100,10))
print(calculate_discounted_price(50,50))