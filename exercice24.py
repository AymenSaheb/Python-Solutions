def anagrams(str1, str2):
   
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)


str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")


if anagrams(str1, str2):
    print("True")
else:
    print("False")
