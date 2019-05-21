'''
#16/04/19
name="John"
name += " Mike"
print(name)
'''
'''
list1 = ["Mango", "Orange", "Cashew", "Onion"]
list2 = ["tomato", 20]
print(type(list2))
#list1 += 5
#print(list1) #will return an objejct bcos an int is not iterable
print(list1 + list2)
list2 += ["Cherry", "Bananas"]
print(list2)


#returns the sum of all valid inputs,
#drops every iinvalid input politely.
total = 0
count = 0
while True:
	try:
		line = input("enter a number: ")
		if line:
			try:
				number=float(line)
			except ValueError as ve:
				print(ve)
				continue
			total += number
			count += 1
		print(total)
	except EOFError:
		break
'''

'''
#Using Functions
def add():
	a = float(input("Enter the first number: "))
	b = float(input("Enter the second number: "))
	print(a + b)
add()
'''


def get_int():
	try:
	 i = int(input("Enter a number: "))
	 print("Your age is ",i)
	except ValueError as ve:
		print(ve)
get_int()