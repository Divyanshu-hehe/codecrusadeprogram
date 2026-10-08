# Write a program to check if a string is a palindrome
a="deb"
rev=""
for ch in a:
    reverse=ch + rev
    if(rev==a):
     print("palindrome")