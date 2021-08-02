# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python

import re

def valid_ISBN10(isbn): 
    #Validate ISBN is correct format first
    if re.match('^[\d]{9}[\d|X]{1}$',isbn):
        isbn =  [int(i) if i != 'X' else 10 for i in isbn]
        return sum([(i+1)*val for i,val in enumerate(isbn)]) % 11 == 0
    return False
