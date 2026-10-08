# Write a program to check if a number is a palindrome.
#     - Example: 121 → palindrome, 123 → not
num=121
a=num
rev=0

while  a!=0:
    temp=a%10
    rev=(rev*10)+temp
    a=a//10
if(rev==num):
    print ("palindrome")
else:
    print("not palindrome")
   