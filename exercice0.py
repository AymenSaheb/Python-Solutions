people = int(input("How many people need a ride?"))
taxi_fit = int(input("How many people fit in one taxi?"))
if people%taxi_fit==0 :
 print(f"Number of taxis needed:{people//taxi_fit}");
else:
    print(f"Number of taxis needed:{people//taxi_fit+1}");