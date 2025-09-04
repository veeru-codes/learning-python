# truthiness
# in python, all conditional checks resolve to True or False
# we can call values that will revolve to True or values that will revolve to False
# besides False conditional checks, other things that are naturally falsy include:
# - empty objects, empty strings, None, and zero

# comparison operators --> ==, !=, >, <, >=, <=
# logical operators --> and, or, not

age = 6
if not ((age >= 2 and age <= 8) or age>=65) :
    print('you pay 10 dollars and are not a child or senior')
else:
    print('you are a child or senior')

city = input('where do you live? ')
if city == 'los angeles' or city == 'san francisco':
    print('you live in california')
else:
    print('you live somewhere else')

# is vs ==
# in python, '==' and 'is' are very similar comparators, however they are not the same

a = 1
print(a == 1) # True
print(a is 1) # True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # True  --> shallow comparison
print(list1 is list2) # False --> deep comparison