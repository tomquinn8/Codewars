# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    x, y = 0, 1
    while x * y < prod:
        x, y = y, x + y
    return [x, y, x * y == prod]
