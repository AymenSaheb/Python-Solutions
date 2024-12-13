letter1 = input("Enter first letter: ").lower()
letter2 = input("Enter second letter: ").lower()
letter3 = input("Enter third letter: ").lower()
Tab_letters = [letter1, letter2, letter3]
Tab_letters.sort()
middle_letter = Tab_letters[1]
print(f"The middle letter is: {middle_letter}")
