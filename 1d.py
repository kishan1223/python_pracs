# Python Program to Reverse a Number using While loop by using function
def reverse_number(number):
 reverse = 0
 while(number > 0):
     remainder = number %10
     reverse = reverse *10 + remainder
     number = number // 10
     print("Reverse number is ", reverse)
reverse_number(12345)

'''n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)'''
