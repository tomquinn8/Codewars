# https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    return ' '.join([''.join([MORSE_CODE[c] for c in word.split()]) for word in morse_code.split('   ')]).strip()
