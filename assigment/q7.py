# Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.
a=int(input("enter the number"))
b=int(input("enter the number"))
if(a%2==0) and (b%2==0) :
    print("both is even")
elif(a%2!=0 and b%2!=0):
    print("both is odd")

else:
    print("one is even and other one is odd")