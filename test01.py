# Coded by Alex Precious
# 1
# Write a bunch of code that prints your name 100 times.

for count in range(1, 101):
    print(f"{count}  Alex Precious")




# 2
# Write a python program that prints the square of integers from 1 - 20.

count = 0
while count < 20:
    count+=1
    print(f"{count} --- {pow(count, 2)}")



# 3a
# Using a for loop, create the shapes below.
# Draw a triangle:

for line in range(6):
    output = ''
    for count in range(line):
        output += '*'
    print(output)


# 3b
# Draw a rectangle
square = [20, 2, 2, 20]
space = " "
for item in square:
    output = ''
    if item == 2:
        print(f'*{space * 18}*')
    else:
        for count in range(item):
            output += '*'
    print(output)

#3c
#Draw an A shape
for item in range(4):
    if item == 0:
        print(f'    ' + f'*' + f'   ')
    elif item == 1:
        print(f'  ' + f'*' + f'   ' + f'*' + f'  ')
    elif item == 2:
        print(f' ' + f'*  ' + f'*  ' + f'*' + f'  ')
    elif item == 3:
        print(f'' + f'*' + f'       ' + f'*' + f' ')
    else:
        print(f'*' + f'   ' + f'*')

#4
#Implement a recursive function that does f(n) = 3^n!
    def factorial(n):
        if n == 1:
            return 1
        else:
            n_factorial = n * factorial(n-1)
            return n_factorial

print(factorial(3))

#5
#Complete last week's assignment

def factorial(n):
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        while True:
            print(f"The {n-1}th factorial is {s}")
            return s


print(factorial(4))
