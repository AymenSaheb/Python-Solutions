print("Runner 1:")
name1=str(input("enter the name of the first runner:"))
time1=float(input("enter the time of the first person(in secondes):"))
print("Runner 2:")
name2=str(input("enter the name of the second runner:"))
time2=float(input("enter the time of the second runner (in secondes):"))
if time1<time2:
    print(f"the faster runner is {name1}")
elif time1==time2:
    print(f"{name1} and {name2} have the same time")    
else :
    print(f"the faster runner is {name2}")