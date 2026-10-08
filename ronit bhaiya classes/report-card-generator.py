print("welcome to report card generator")
name=input("enter your name:")
dsa_score=float(input("enter your dsa score:"))
oops_score=float(input("enter your oops score:"))
maths_score=float(input("enter your maths score:"))
total_score=dsa_score+oops_score+maths_score
percentage=(total_score/300)*100
is_eligible=percentage>=90
print(f"\nReport Card for {name}:")
print(f"DSA Score: {dsa_score}")
print(f"OOPs Score: {oops_score}")
print(f"Maths Score: {maths_score}")
print(f"Total Score: {total_score}")
print(f"Percentage: {percentage:.2f}%")
print(f"Eligible for Scholarship: {is_eligible}")