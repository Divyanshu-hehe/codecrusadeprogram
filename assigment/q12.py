# Print the reverse of a given number.
a=1234

rev=0
while a>0:
    rev=rev*10 +a%10
    a//=10
print(rev)