word=str(input("please enter the word to check: "))
Table=list(word)
i=0
is_palindrome=True
for i in range(len(Table) // 2):  
    if Table[i] != Table[-(i + 1)]: 
        is_palindrome = False
        break

if is_palindrome:
   print("yes,it's a palindrome")
else :
   print("no,it's not a palindrome")
