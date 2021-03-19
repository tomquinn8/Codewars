# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    numbers = [i for i in numbers if i >=0] #Remove negative numbers
    numbers.sort()
    return numbers[0] + numbers[1]
