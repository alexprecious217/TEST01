'''
#9/04/19
#identity operators
a = ["today", "tomorrow", True, 0.5, False]
b = ["today", "tomorrow", True, 0.5, False]
print(a is b)
print(a is not b)
a=b
print(a is b)
print(a is not b)



#comparison operators
a=2
b=6
print(a<b)
print(a>b)

#in python we can chain comparison operators:
a=9
print(0 <= a <=10)
#python is strongly dynamically typed. We do not need to supply the object.
'''
'''
#membership operators
p = (4, "monkey", 10, -33, True)
print(2 in p)
print(2 not in p)

q = "Today is Tuesday"
print("Today" in q)
'''
'''
a = "Monday"
b = "Tuesday"
print(a and b)
print(a or b)

'''
'''
#				Control Flow Statements

#the if-else statement:
if condition1:
	pass
elif condition2:
	pass
'''
'''
else:
	pass
'''


'''
#11/04/19
#The while loop: this is used to test if a condition returns true, more than once.The break statement is used to break out of a loop. The continue statement is used to push the programme back to the beginning of the loop.
lessThan5 = 0
while lessThan5 < 5:
	print("still < 5")
	lessThan5 += 1
	if lessThan5==3:
		break
	print("Thank you")
print("finished")
'''
'''
lessThan5=0
while lessThan5 < 5:
	print("Still < 5")
	lessThan5 += 1
	if lessThan5==3:
		continue
	print("I'm waiting")
'''
'''
countries = ["Nigeria", "Ghana", True, 1000, "America"]
for item in countries:
	print(item)
'''

'''
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
for alphs in alphabets:
	if alphs in vowels:
		print(alphs + "is a vowel")
	else:
		print(alphs + "is a consonant")


#Exceptions are situations that have not been considered by the programmer.
try:
	x = int(input("Enter a number: "))
	ansa = x/2
	print(ansa)
except ValueError as err:
	print(err)

print("There are three numbers." + \
	"The first is {0:d}, the second is {1:1d} and the last but not the least is {2:2d}.".format(2,5,8))

import datetime

today = datetime.date.today()
print(today)
'''

from datastructures import morse
print(len(morse))