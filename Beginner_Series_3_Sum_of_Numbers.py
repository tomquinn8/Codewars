# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a,b):
    return sum(i for i in range(min(a,b),max(a,b)+1))
