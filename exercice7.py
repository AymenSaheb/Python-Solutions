year=int(input("please enter the year:"))
leap_year=False
if year % 4==0:#dans la premiere conditipon on verifie si l'annee est divisible par 4 si non on sort de la boucle
  if year % 100==0:#on verifie si l'annee est divisble par 100 on verifie si elle est divisible par 400 sinn elle esr leap year
    if year % 400==0:
      leap_year=True
  else: 
   leap_year=True   
if leap_year : 
    print("That year is a leap year")   
else :
    print("That year is not a leap year")         
            