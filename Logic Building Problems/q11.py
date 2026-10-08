# Write a program to count the number of vowels in a string.
a="hello"
count =0
vowels="aeiou"
for ch in a:
    if ch in vowels:
        count+=1
    else:
        continue
print(count)