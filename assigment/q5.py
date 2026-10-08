# Take the hour of the day (0-23) and print "Good Morning", "Good Afternoon", "Good
# Evening", or "Good Night".
hour=int(input("enter time"))
if(hour>=0 and hour<12):
    print("good morning divyanshu")
elif(hour>=12 and hour<18):
    print("good afternoon divyanshu")
elif(hour>=18 and hour<22):
    print("good evening divyanshu")
elif(hour>=22 and hour<24):
    print("good night divyanshu")
else:
    print("kuch bhi mtlb ")