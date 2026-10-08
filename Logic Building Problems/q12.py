# Write a program to reverse a string without using slicing.
# a="hello"
# rev=""
# for i in range(len(a)-1,0,-1):
#     rev+=i
#     print(rev)
a = "hello"
reverse = ""

for ch in a:
    reverse = ch + reverse
print(reverse)