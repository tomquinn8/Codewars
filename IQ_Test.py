# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    numbers=list(enumerate(numbers.split(), 1))
    odds = [i for i in numbers if int(i[1]) % 2 > 0]
    evens = [i for i in numbers if int(i[1]) % 2 == 0]
    if len(odds) < len(evens):
        return odds[0][0]
    else:
        return evens[0][0]
