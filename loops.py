#Toluwalope Omonale
#A0020211

#Problem 1
lyrics = list(range(1, 100))
lyrics.reverse()
for i in lyrics:
    print( i, "bottles of coke on the wall,", i, "bottles of coke.")
    print("take one down and pass it around,", i-1, "bottles of coke on the wall.")


#Problem 2
year1= int(input("What is the first year?:"))
year2= int(input("What is the other year?:"))
for n in range(year1, year2+1):
    if n % 4 == 0:
         if n%100 != 0:
             print(n, end=" ")
         elif n%400 == 0:
             print(n, end=",")


#Problem 4
x = int(input("Give a number:"))
gap = 0
for n in range(1, x+1):
    tri = (2*n)-1
    print(gap*" ", end="")
    print(tri*".", end="")
    n+=1
    print()
    # gap-=1


#Problem 3
n = int(input("Give a number:"))
y = 0
a = 1
while n != 1:
       print(n, end=",")
       if n % 2 == 0:
           n = n // 2
       else:
           n = n * 3 + 1
       a+=1
       y+=1
       if y == 10:
           print()
           y = 1
print(n, end=" ")

# print("\n There are ", x, "numbers in this sequence")

