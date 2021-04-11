# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(strng):
    numbers = re.search( r'\d+$', strng)
    if not numbers:
        return strng + '1'
    else:
        return strng.replace(numbers[0],str(int(numbers[0]) + 1).zfill(len(numbers[0])))
