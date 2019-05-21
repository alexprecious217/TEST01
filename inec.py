print("Welcome to The INEC's official App")
try:
	buhari = int(input("No. of Buhari's vote: "))
	print("You entered %i votes for Buhari." %buhari)

	Atiku = int(input("No. of Atiku's vote: "))
	print("You entered %i votes for Atiku." %Atiku)

	inconclusive = int(input("No. of inconclusive states(if any): "))
	if inconclusive > 36:
		print("You have exceeded the maximum number of states")
	elif inconclusive >= 5:
		print("Sorry, the election has to be cancelled.")
	else:
		stateBu = int(input("How many states did buhari win?: "))
		stateAt = int(input("How many states did atiku win?: "))
		if stateBu + stateAt > 36 - inconclusive:
			print("You have exceeded the maximum number of states")
		elif stateBu > stateAt:
			print("Buhari is the WINNER!!!")
		elif stateAt > stateBu:
			print("Atiku is the WINNER!!!")
		else:
			print("Please the election has to be re-run")
except ValueError:
	print("Please input the right value.")