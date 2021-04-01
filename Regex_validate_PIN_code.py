# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

import re

def validate_pin(pin):
	return True if re.match("^\d{4}\Z|^\d{6}\Z",pin) else False

print(validate_pin("1"))
print(validate_pin("12"))
print(validate_pin("123"))
print(validate_pin("12345"))
print(validate_pin("1234567"))
print(validate_pin("-1234"))
print(validate_pin("123456"))
print(validate_pin("1234\n"))


