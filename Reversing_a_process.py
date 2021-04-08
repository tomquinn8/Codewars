# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python

def decode(r):
    number = int(''.join([x for x in r if x.isnumeric()]))
    string = ''.join([x for x in r if x.isalpha()])
    moduli = [(i * number % 26, i) for i in range(26)]
    decoded  = ''
    for c in string:
        options = [i for x,i in moduli if x == ord(c)-97]
        if len(options)!=1:
            decoded = 'Impossible to decode'
            break
        decoded += chr(options[0]+97)
    return decoded
