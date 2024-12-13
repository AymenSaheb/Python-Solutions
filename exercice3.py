Total_amount=float(input("please enter the total amount of purshase:"))
Number_of_items=int(input("please enter the number of items:"))
Day_of_the_week=str(input("enter the day of the week:")).lower()

if Day_of_the_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    Price_after_discount=Total_amount-Total_amount*0.1
elif Day_of_the_week in ["saturday", "sunday"]:
    Price_after_discount=Total_amount-Total_amount*0.2
if Number_of_items>5:
    Price_after_discount=Total_amount-Total_amount*0.05   

print(f"Total amount: {Total_amount}")
print(f"Number of items: {Number_of_items}")
print(f"Day of the week: {Day_of_the_week}")
print(f"Total price after discount: {Price_after_discount} dinars")    