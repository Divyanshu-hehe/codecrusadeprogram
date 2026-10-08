# Count the number of digits in a given number.
a=1234
count=0 
while a>0:
    a//=10
    count+=1
print(count)