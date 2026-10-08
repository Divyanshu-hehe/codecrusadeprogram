# for i in range(10,0,-1):
#     print(i)
# n=int(input("enter number"))
# sum=0
# for i in range(1,n+1,1):
#     if n%2==0:
#         sum+=i
# print(sum)
# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
# Print the product of digits of a given number.
a=1234
temp=a
pro=1
for i in str(temp):
    temp=a%10
    pro*=temp
    temp//=10
print(pro)

