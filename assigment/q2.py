# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
# scalene.
a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if (a==b==c):
    print("it is a equilateral triangle")
elif(a==b)or(c==a) or(c==b):
    print("it is a isosceles triangel")
else:
    print("scalene triangle")