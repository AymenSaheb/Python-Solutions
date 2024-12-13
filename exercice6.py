price=float(input("Please type in a price:"))
dinars=int(price)
centimes=int((price - dinars) * 100 ) #1 Dinar = 100 Centimes donc la partie decimale doit etre composee de 2 chiffre
print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")