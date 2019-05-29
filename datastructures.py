#Lists
'''
list1 = ['Mathematics', 'Language', 'Science', 2000, False, 'Health Education']
'''
'''
print(type(list1))

print(list1[2])

#Updating the list
list1[4] = True
print(list1)
#Deleting items from the list
del list1[2]
print(list1)

#Multiplication and concatenation
list2 = list1 + ['Agric', '10.7']
print(list2)
print(['Agric', '10.7'] * 3)

#Lenght of list
print(len(list1))

#Membership
print('Agric' in list1)
'''

'''
#Iteration
print("Start Iteration")
for x in list1:
    print(x, list1.index(x))


'''
'''
list1 = ['Mathematics', 'Language', 2000, True, 'Health Education']
for x in list1:
    print(x, end=" ")#This prints the whole list items but on the same line similar to a list
    print(x)#This prints the whole list vertically on different lines
'''
'''


for x in list1:
    if (list1.index(x) <= 3):
        print(x, end=' and ')
    else:
        print(x)
'''
'''
#Indexing
print(list1[-2])
'''
'''
#max
list2 = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Wednesday']
print(max(list2))
'''

'''
#convert a tuple to list
tuple = (234, 'C++', False, 'Python')
list3 = list(tuple)
print(list3)
list4 = list3.append('Cee#')
list5 = list3 + ["C#"]
print(list3)
print(list4)
print(list5
'''
'''
#To count items in a list
list6 = [234, 'C++', False, 'Python', 'C++', 'C#']
print(list6.count("C++"))

print([234, 'C++', False, 'Python', 'C++', 'C#'].count('Python'))
print([234, 'C++', False, 'Python', 'C++', 'C#'].count('Jython'))
'''

'''
#To print a range
for i in range(5):
    print(i, end=' ')
'''
'''
list7 = list(('a', 'b', 'c', 'd'))
print(list7)
new = list7.extend(range(5))
print(list7)
print(new)
'''
'''
#Dictionaries
states_pop = {"Lagos":3546789, "Kano":46789045, "Abuja":1234556, "Port-Harcourt":55673484, "Kaduna":2456782}
print(states_pop['Kano'])
print(states_pop[1])


en_yor = {'One':'Ookan', 'Two':'Eeji', 'Three': 'Eeta', 'Four':'Eerin', 'Five':'Aarun' }
#print(en_yor['Two'])

yor_ibo = {'Ookan':'otu', 'Eeji':'abuo', 'Eeta':'ato','Eerin':'ano', 'Aarun': 'ise'}

#print(yor_ibo['Eeta'])

print(yor_ibo[(en_yor['One'])])
print(yor_ibo[en_yor['Two']])


#Rules or using dictionaries. We cant use mutable types as keys. A mutable type of data is a type of data that can be changed, eg, lists.
#dic = {[1,2,3]:'abc'}
dic = {'abc':[1,2,3]}

#Operations on dictionaries
# len(), del k[], for k in dic, k not in dic
print('abc' in dic)
del dic['abc']
print(len(dic))


morse = {
    'A':"qw",
    'B':"qwe",
    'C':"qwerty",
    'D':"qwertyui",
    'E':"qwertyuiop",
    '1':"as",
    '2':"asdf",
    '3':"asdfghj",
    '4':"asdfghjkl",
    '5':"asdfghjklxz"
}
from datastructures import morse
print(len(morse))


#pop() method
en_yor = {'One':'Ookan', 'Two':'Eeji', 'Three': 'Eeta', 'Four':'Eerin', 'Five':'Aarun' }
print(en_yor.pop('Three'))


#Classwork
en_yor = {'One':'Ookan', 'Two':'Eeji', 'Three': 'Eeta', 'Four':'Eerin', 'Five':'Aarun' }
yor_ibo = {'Ookan':'otu', 'Eeji':'abuo', 'Eeta':'ato','Eerin':'ano', 'Aarun': 'ise'}
print("Language Translator:Ibo")
trans = input("Enter an English word: ")
psuedoTrans = trans.capitalize()
print(yor_ibo[en_yor[psuedoTrans]])


#30/04/19
#merging dictionaries:
#copy():
capitals1 = {"Nigeria":"Abuja", "Mali":"Bamako", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg"}
capitals2 = {"United States": "New York", "Russia":"Moscow", "Sweden":"Stockholm"}
###print(capitals1)


#iterating over a dictionary
#print all the items in the updated capitals1 dictionary
for countries,capitals in capitals1.items():
    print(countries + capitals)
'''
#conversion between lists and dictionaries:
capitals1 = {"Nigeria":"Abuja", "Mali":"Bamako", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg"}
print(type(capitals1))
list1 = list(capitals1)
print(list1)
print(type(list1))
print(list1[3])