# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    firstnumber = (int(((n*(n+1))/2)-n)*2)+1
    return sum(range(firstnumber, firstnumber +(n*2),2))
