Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def len(s):
	count = 0
	for i in s:
		if i != '':
			count +=1
	print("The total length of string is: ", count)
	return count

>>> s = 'god is great'
>>> len(s)
The total length of string is:  12
12
>>> 