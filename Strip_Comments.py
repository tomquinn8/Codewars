# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

import re

def solution(string, markers):
    for marker in markers:
        string = re.sub(r'\ *[/' + marker + ']+.*(\n|$)', r'\1', string)
    return string
