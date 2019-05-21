#simply prints the argument passed to it
'''
def writer (arg):
    print(arg)
writer("Hello class")

#converts celcius to fahrenheit:

#def fahren(T_in_celcius):
 #   return T_in_celcius * 9/5 + 32
#print(fahren(20), "fahrenheit")

fahren_list = []
celcius_list = [20, 5, 10.6, 7, 9]
for x in celcius_list:
    fahren_list.append(fahren(x))
print(fahren_list)


#change a list passed to it:

number1 = int(input("enter numbers"))
number2 = int(input("enter numbers"))
number3 = int(input("enter numbers"))
number4 =int(input("enter numbers"))
number5 = int(input("enter numbers"))

number = number1 + number2 + number3 + number4 + number5
new_number = number/2
print(new_number)


def average():
    list = []
    sum = 0

    x=0
    while len(list) <= 3 :
        item = float(input("enter a number"))
        list.append(item)
        x += 1
    print(list)

    for item in list:
        sum += item
    av = float(sum/len(list))
    print(av)
 
    

#average()



#list = ['money is good']
#print(len(list))
#print(list[0])


#14/05/19
#Keyword parameters:
def sum(a, b, c=0, d=0):
    return a-b+c-d
print(sum(10, 5))
print(sum(12, 3, 6))

#variable scoping:
#global variables are accesible within and without a function.
def f():
    print(s)
s="Python"
f()


def f():
    s = 'Clojure'
    print(s)
f()

def f():
    s='Person'
    print(s)


s='Python'
f()
print(s)

#The value of a global variable can be changed inside a function.
def f():
    global s
    print(s)
    s='bird'
    print(s)


s='cow'
f()
print(s)


#Arbitrary number of parameters:
def arithmetic_mean(num1, *values):
    return (num1 + sum(values)) / (1 + len(values))


print(arithmetic_mean(45, 86, 90, 77))
print(arithmetic_mean(87, 90))


#Classwork:
def sum_gp(num1, num2, num3):
    return (num1 * (pow(num2, num3) - 1)) / (num2 - 1)


first_term = int(input("Enter the first term: "))
ratio = int(input("Enter ratio: "))
size = int(input("Enter the size: "))
sum = (sum_gp(first_term, ratio, size))
print(sum)


#Classwork2:
def average(num1, *param):
    return (num1 + sum(param)) / (1 + len(param))


print(average(2, 3, 4, 5, 6, 7))
print(average(2, 3, 4))
'''

#Recursive Functions:

def factorial(n):
    if n == 1:
        return 1
    else:
        r = 0
        r+=1
        s = n * factorial(n-1)
        while True:
            print(f"The {n}th factorial is {s}")
            return s




print(factorial(5))








