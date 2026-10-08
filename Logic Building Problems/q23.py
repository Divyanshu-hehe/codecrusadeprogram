# rite a program to find the sum of digits of a number.
#     - Example: 1234 → 1+2+3+4 = 10
a=1234
b=0

while a!=0:
    temp = a%10
    b += temp
    a = a//10

print(b)
    