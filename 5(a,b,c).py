Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> released={'Python 3.6': 2017,'Python 1.0': 2002, 'Python 2.3': 2010}
>>> for key,value in sorted(released.items()):
	print (key,value)

	
Python 1.0 2002
Python 2.3 2010
Python 3.6 2017
>>> print (sorted(released))
['Python 1.0', 'Python 2.3', 'Python 3.6']
>>> dic1={1:10, 2:20}
>>> dic2={3:30, 4:40}
>>> dic3={5:50,6:60}
>>> dic1.update(dic2)
>>> print (dic1)
{1: 10, 2: 20, 3: 30, 4: 40}
>>> dic1.update(dic3)
>>> print (dic1)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
>>> d= {'One':10,'Two':20,'Three':30}
>>> sum(d.values())
60
>>> 
>>> 