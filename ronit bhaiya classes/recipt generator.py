print("welcome to recipt generator")
item1=int(input("enter the cost of item1"))
item2=int(input("enter the cost of item2"))
item3=int(input("enter the cost of item3"))
total_cost=item1+item2+item3
if total_cost>2000:
    discount=total_cost*0.1
    final_cost=total_cost-discount
    print(f"total cost:{total_cost}")
    print(f"total dicount:{discount}")
    print(f"final cost:{final_cost}")
elif total_cost>1500:
    discount=total_cost*0.05
    final_cost=total_cost-discount
    print(f"total cost:{total_cost}")
    print(f"total dicount:{discount}")
    print(f"final cost:{final_cost}")
else:
    print("discount not applicable")
    print(f"total price:{total_cost}")