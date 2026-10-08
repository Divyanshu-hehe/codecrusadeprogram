# Take marks (0-100) and print the corresponding grade (A/B/C/D/F).
grade=int(input("enter your grade"))
if(grade>90):
    print(f"your grade is A")
elif(grade>=70 and grade<90):
    print("your grade is B")
elif(grade>=50 and grade<70):
    print("your grade is c")
elif(grade>=30 and grade<50):
    print("your grade is D")
else:
    print("you are failed ")