# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

import math

def isPP(n):
    for i in range(int(n ** 0.5) + 1, 1, -1):
        log = int(round(math.log(n, i)))
        if i ** log == n:
            return [i, log]
    return None
