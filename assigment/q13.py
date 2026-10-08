# check if a number is a palindrome
a=121
rev=0
while a>0:
    rev=rev*10+a&10
    a//=10
    if