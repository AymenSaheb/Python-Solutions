name=str(input("please enter your name:")).lower()
if name=='vip':
    print("Enjoy the show for free! ")
else:
    nb_tickets=int(input("How many ticket would you like to buy?"))
    print(f"the total cost is:{nb_tickets*15.50}")  
    print("enjoy your tickets!")