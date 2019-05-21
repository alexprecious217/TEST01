'''
list1 = ['Mathematics', 'Language', 'Science', 2000, False, 'Health Education']
print(type(list1))
#access the nth item
print(list1[2])

#updating the list
list1[4] = True
print(list1)

#deleting items from a list
del list1[2]
print(list1)

#multiplication and concatenation
list2 = list1 + ['Agric', '10.7']
print (list2)
print(['Agric', '10.7'] * 3)

#length of list1
print(len(list1))

#membership
print('Agric' in list2)

#Iteration
print("start iteration")
for x in list1:
    print(x)

print("start from here:")
for x in list1:
    if(list1.index(x) <= 2):
        print(x)

'''

list1 = ['Mathematics', 'Language', 2000, True, 'Health Education']
'''
for x in list1:
    print(x)
'''
'''
for x in list1:
    print(x, end=' and ')
'''
'''
print("start again from here:")
for x in list1:
    if(list1.index(x) <= 3):
        print(x, end=" and ")
    else:
        print(x)
'''
'''

#Indexing
print(list1[-2])
print(list1)
print ("slicing starts")
print(list1[2:])
print(list1[:2])
print (list1[1:4])

#max
list2 = ['Monday', 'Tuesday', 'Thursday', 'Fridayday', 'Wednesday']
print(max(list2))

#convert a tuple to list
tuple1 = (234, 'C++', False, 'Python')
list3 = list(tuple1)
print (list3)

#append()
list3 = [234, 'C++', False, 'Python']
list4 = list3.append('Cee#')
list5 = list3 + ["c#"]
print (list5)
print (list4)

#count:
list6 = [234, 'C++', False, 'Python', 'C++', 'c#']
print(list6.count("C++"))

print([234, 'C++', False, 'Python', 'C++', 'c#'].count("Python"))
print([234, 'C++', False, 'Python', 'C++', 'c#'].count("Jython"))

#extending a range into a list
print(range(5))
for i in range(5):
    print(i, end=" ")

list7 = list(("a", "b", "c", "d"))
print (list7)
new = list7.extend(range(5))
print (list7)
print(new)
'''
'''
#index
names = ['bolaji', 'aisha', 'daniel', 'david', 'aisha', 'taofeek']
print('first occurence of aisha', names.index('aisha'))

#pop() : returns and removes the last item
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
print(subjects.pop())
print(subjects.pop())


#remove() : removes the item but it returns None
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
holder1 = subjects.pop()
holder2 = subjects.remove('english') #a compulsory argument

print(holder1)
print(holder2)


#reverse: reverses the list list and returns None:
subjects = ['maths', 'english', 'science', 'language', 'culture', 'religion']
holder3 = subjects.reverse()
print(holder3)
print((subjects))

#sort():
subjects = ['maths', 'Maths', 'english', 'science', 'language', 'culture', 'religion']
numbers = [12, 6, 3, 98]
print(numbers.sort())
print(numbers)
print(subjects.sort())
print(subjects)


#Dictionaries
states_pop = {"Lagos":3567234, "Kano":46742871,
    "Abj":1672357, "Ph":3123907, "Kad":2784123
    }
print(states_pop['Kano'])
#KeyError
#print(states_pop['Kogi'])
#print(states_pop[1])

states_pop['Ogun'] = 3123578
print(states_pop)

states_pop['Kano'] = 123785
print(states_pop)

#defining an empty dictionary:
names = {}
names['first'] = "Seun Bala"
print(names)

#the keys and thevalues can both recur:
name = {'first':'Seun Bala', 'second':'John Udeh',
        'first':'Mark Thaindi',
        'fourth':'Seun Bala'
        }
print(name['first'])


en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta',
          'four':'eerin', 'five':'aarun'
          }
#print(en_yor['two'])

yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato',
           'eerin':'ano', 'aarun':'ise'
           }
print(yor_ibo['eeta'])
#classwork: eng_ibo translations of 'one', 'two'
print(yor_ibo[en_yor['one']])
'''
#Rules
#we can't use mutable types as key
#dic = {[1,2,3]:'abc'}
dico = {'abc':[1,2,3]}
'''
#Operations on Dictionaries
#  len(d), del(k), k in d, k not in d
dico.__delitem__('abc')
print('abc' in dico)
del dico['abc']
print(len(dico))
print(dico)

morse = {
    'A': "qw",
    'B': "qwer",
    'C': "qwerty",
    'D': "qwertyui",
    'E': "qwertyuiop",
    '1': "as",
    '2': "asdf",
    '3': "asdfghj",
    '4': "asdfghjkl",
    '5': "asdfghjklxz"
}
from datastructures import morse
print(len(morse))


#pop()
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta',
          'four':'eerin', 'five':'aarun'
          }
#print(en_yor.pop('one'))
#print(en_yor.pop('three'))

#If a pair cannot be popped, a key error is raised:
#print(en_yor.pop('six'))
print(en_yor.pop('one', 'placeholder'))
print("Hello world")
'''
#popitem()
'''
capitals1 = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome",
            "South Africa":"Johannesburg", "Mali":"Bamako"}

print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
#print(capitals.popitem())
print((capitals))


#we can prevent the errors from passing non-existent keys using the membership operator:
#print(capitals["Rivers"])

if "Rivers" in capitals:
    print(capitals["Rivers"])

#alternative, get()
print(capitals.get("Nigeria", "Port Harcourt"))


#Merging Dictionaries:
capitals1 = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome",
            "South Africa":"Johannesburg", "Mali":"Bamako"}

capitals2 = {"United Kingdom":"London", "Russia":"Moscow", "Sweden":"Stockholm"}
updated_dic=capitals1.update(capitals2)
print(updated_dic)
print(capitals1)

#Iterating over a dictionary:
#print all the items in the updated capitals1 dictionary
'''

#Conversion Between Lists and Dictionaries:
capitals1 = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome",
            "South Africa":"Johannesburg", "Mali":"Bamako"}, {"United Kingdom":"London", "Russia":"Moscow", "Sweden":"Stockholm"}
print((type(capitals1)))
list1 = [capitals1]
print(type(list1))
print(list1[0])






