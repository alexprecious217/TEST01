'''
print("Welcome to Alli's Personalized Short Stories\n")

print("Please enter your necessary details")

name = input("What is your name?: ")
state = input("What satte are you from?: ")
parent = input("What is your parent's name?: ")
age = input("How old are you?: ")
gender = input ("your gender: ")

print(name.upper(), "is a " + age, "year old " + gender,".")
if gender = "male":
	print(name.upper(), "has lost his memory.")
	print("He can't remember who he is or where he came from. He only knows he fell through " + state.upper(),".")
	print("He claims there's a forgotten door from " + state.upper(), "to this strange planet, Earth, and he is in great danger.")
	print("Injured from the fall, he has to find " + parent.upper(), "who are his parents, to help him.")

else:
	print(name.upper() + "has lost her memory.")
	print("She can't remember who she is or where she came from. She only knows she fell through " + state,".")
	print("She claims there's a forgotten door from " + state + "to this strange planet, Earth, and she is in great danger.")
	print("Injured from the fall, she has to find " + parent.upper() + "who are her parents, to help her.")
'''
'''
print("Welcome to the Addison O'Reiley Sales Tax Programme!\n")

salePrice = float(input("Enter the sales price: =N="))
print("=N=",salePrice)
taxRate = float(input("Enter the sales tax rate: "))
print(taxRate,"%")
saleTax = salePrice * taxRate
cost = saleTax + salePrice

print("Total cost: =N=",cost) 
'''


totalPurchase = float(input("Enter total purchase: $"))
if totalPurchase < 50:
	print("You've been charged $10 extra for shipping.")
	print("Total charge = $",totalPurchase + 10)
else:
	print("Your shipping is free.")
	print("Total charge = $", totalPurchase)
print("thanks for patronizing us.")