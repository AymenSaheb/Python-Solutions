tableau = []
mot = ""  

while mot != "stop":
    mot = input(f"please enter the names of the cities 'or stop to stop': ")
   
    if mot != "stop":  
         tableau.append(mot)

for mot in tableau:
    Length=len(mot)
    print(f'The city "{mot}" has {Length} letters, so its population is {Length*1000000}.')