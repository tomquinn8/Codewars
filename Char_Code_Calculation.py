# https://www.codewars.com/kata/57f75cc397d62fc93d000059

def calc(x):
	total1 = ''.join([str(ord(i)) for i in x])
	total2 = total1.replace("7","1")
	return sum([int(x) for x in total1]) - sum([int(x) for x in total2])


print(calc("abcdef"))
print(calc("ifkhchlhfd"))
print(calc("aaaaaddddr"))
print(calc("jfmgklf8hglbe"))
print(calc("jaam"))
