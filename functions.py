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
number4 = int(input("enter numbers"))
number5 = int(input("enter numbers"))

number = number1 + number2 + number3 + number4 + number5
new_number = number/2
print(new_number)


def average():
    list = []
    sum = 0
    x=0
    while len(list) <= 3:
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


#Recursive Functions:

def factorial(n):
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        while True:
            print(f"The {n-1}th factorial is {s}")
            return s



print(factorial(7))


space = " "
for bum in range(5):
    output = ''
    print(f"{output * 5}  blah balh blah")


#28/05/19
def factorial(n):
    print(f"factorial has been called with n= " + str(n))
    if n == 1:
        return 1
    else:
        result = n*factorial(n-1)
    print(f"the immediate result for {n}: {result}")
    return result


factorial(5)

def while_factorial(n):
    res = 1
    i=0
    while(i<n):
        i+=1
        res *= i
    return res


print(while_factorial(6))

def for_factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return  res

print(for_factorial(6))



#To return the nth fibonacci series
def fib(n):
    n1 = 0
    n2 = 1
    count = 0
#check if the number of terms is valid
    if n_term <= 0:
        print("Please enter a positive integer.")
    elif n_term == 1:
        print("Fibonacci sequence up to", n_term, ":")
        print(n1)
    else:
        print("Fibonacci sequence up to", n_term, ":")
        while count < n_term:
            print(n1, end=",")
            nth = n1 + n2
    #To update the value
            n1 = n2
            n2 = nth
            count += 1



n_term = int(input("Please input the nth term: "))
fib(n_term)

#returning the nth fibonacci number
#Using the recursive method
import time
t2=time.time()
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(7))
'''

import time
t1=time.time()
#Using the iterative method
def fib_iterative(n):
    old, new = 0, 1
    if n==0:
        return 0
    for i in range(n-1):
        old, new = new, old+new
    return new


print(fib_iterative(9))
print(time.time())