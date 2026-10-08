# Write a program to check if a number is prime.
n = 11

if n <= 1:
    print("Not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")