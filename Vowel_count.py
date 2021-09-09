# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    return len([c for c in sentence if c in ['a','e','i','o','u']])
