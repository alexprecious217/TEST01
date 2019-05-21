print("Welcome To Lapo MFBank")

rate = float(input("What is your company's rate: "))
rate_fraction = rate/100
print("Your company's rate is: %.1fpercent" %rate)


principal = float(input("Enter the amount needed: "))
print("you requested %.1f" %principal)

def monthPay():
	time = int(input("Enter the time duration for the loan: "))
	print("The duration for the loan is: %i year(s)" %time)

	interest = (principal * rate_fraction * time)

	total = interest + principal

	monthlyRep = int(total/(time * 12))

	print("Your monthly repayment is: =N=%i" %monthlyRep)


if 0 < rate <= 5 and principal <= 200000:
	monthPay()

	
elif 0 < rate <= 5 and principal > 200000:
	print("Sorry you do not reach the minimum requirement!") 

elif 5 < rate <= 10 and principal <= 500000:
	monthPay()


elif 5 < rate <= 10 and principal > 500000:
	print("Sorry you do not reach the minimum requirement!") 

elif 10 < rate <=20 and principal <= 1000000:
	monthPay()


elif 10 < rate <= 20 and principal > 1000000:
	print("Sorry you do not reach the minimum requirement!") 

elif 20 < rate <=25 and principal <= 1500000:
	monthPay()

elif 20 < rate <= 25 and principal > 1500000:
	print("Sorry you do not reach the minimum requirement!")
	

else:
	monthPay()





