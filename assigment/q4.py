# Check if one of two given numbers is a multiple of the other.
a=int(input("enter your number"))
b=int(input("enter your number"))
if(a%b==0):
    print(f"{a} is multiple of {b}")
elif(b%a==0):
    print(f"{b}is multiple of {a}")
else:
    print("none of them are multiple of each other")