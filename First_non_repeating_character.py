#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python


def first_non_repeating_letter(string):
    single_characters = [c.upper() for c in string if string.upper().count(c.upper()) == 1]
    for c in string:
        if c.upper() in single_characters: return c
    return ''
