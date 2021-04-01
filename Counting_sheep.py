# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
	return sheep.count(True)


array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
	  True,  False, True,  False,
	  True,  False, False, True ,
	  True,  True,  True,  True ,
	  False, False, True,  True ];
print(count_sheeps(array1))	  
