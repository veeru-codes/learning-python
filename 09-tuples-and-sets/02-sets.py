# sets are like formal mathematical sets.
# sets do not have duplicate values
# elements in sets aren't ordered
# sets does not support indexing
# sets can be useful if you need to keep track of a collection of elements,
# but don't care about ordering, keys or values and duplicates

my_set = {1, 2, 3, 4, 3, 2, 1}
print(my_set)

# throws an error: 'set' object does not support indexing
# print(s[0])

print(len(my_set))  # 4
print(5 in my_set)  # False

# looping
for num in my_set:
    print(num)

# generate a list of ten cities with duplicate city names
cities = ['New York', 'Chicago', 'New York', 'Chicago']
cities = set(cities)
print(f"length of cities set: {len(cities)}")

# methods
# add - adds an element to a set. if the element is already in the set, the set doesn't change
# remove - removes a value from the set. returns a KeyError if the value is not found.
# discard - removes a value from the set. but returns nothing if the value is not found.
# copy - creates a copy of the set
# clear - removes all the contents of the set

cities.add('Chicago')
cities.remove('Chicago')
print(cities)

cities_copy = cities.copy()
cities_copy.clear()

# set math
math_students = {"matthew", 'helen', 'prashant', 'james', 'aparna'}
biology_students = {'jane', 'matthew', 'charlotte', 'mesut', 'oliver', 'james'}

# union - to generate a set with all the unique students
print(math_students | biology_students)

# intersection - to generate a set with students who are in both courses
print(math_students & biology_students)
