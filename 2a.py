"""
Write a python program to define a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""
#TYPE 1
#function definition
def is_vowel(char):
    if(char=='a' or char=='A' or char=='e' or char=='E'
       or char=='i' or char=='I' or char=='o' or char=='O'
       or char=='u' or char=='U'):
        print(char, "is a vowel")
    else:
        print(char, "is not a vowel")

#function call
char=input("enter a character: ")
is_vowel(char)
