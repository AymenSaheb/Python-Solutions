string = str(input("Please type in a string: "))
length=len(string)
nb_space=(28-length)//2
if length<=28:
    print('*'*30)
    if length%2==0:
     print('*'+' '*nb_space+string+' '*nb_space+'*')
    else:
     print('*'+' '*(nb_space)+string+' '*(nb_space+1)+'*')
    print('*'*30)
else:
 print('error')