# there is a lambda for each value in the iterable
# returns filter object which can be converted into other iterables
# the object contains only the values that return true to the lambda

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

names = ['austin', 'penny', 'anthony', 'angel', 'billy']
names_with_a = list(filter(lambda name: name[0] == 'a', names))
print(names_with_a)

# combining filter and map
instructors = ['lassie', 'colt', 'rusty']
print(list(map(lambda name: f"your instructor is {name}", filter(lambda name: len(name) < 5, instructors))))
