# Write a program to reverse a number.
#     - Example: 1234 → 4321
a=1234
b=0
while a!=0:
    temp=a%10
    b=(b*10)+temp
    a=a//10
    print(b)