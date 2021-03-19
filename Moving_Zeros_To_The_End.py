# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    return [a for a in array if (a is not 0 and type(a) != float) or (type(a) == float and a>0)] + [int(c) for c in [b for b in array if b == 0] if type(c) != bool]
