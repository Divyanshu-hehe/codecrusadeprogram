# Take three sides and check if they form a valid triangle
a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if((a+b>c)and (b+c>a)) and (a+c>b):
    print("it is a triangle")
else:
    print("not a triangle")
