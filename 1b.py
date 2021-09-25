# python program to check if the input number is odd or even.
# a number is even if division by 2 give a remainder 0.
# if remainder is 1, it is odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))
    
