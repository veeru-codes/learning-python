# .append() - add an item to the end of the list
# .extend() - extend list by appending elements from the iterable.
# .insert() - insert an item at a given position

# .pop()    - remove the item at a given position in the list, and return it.
#           - if no index is specified, removes and returns last item in the list
# .remove() - remove first occurrence of value.
#           - raises ValueError if the value is not present.
# .clear()  - remove all items from the list

# .index()  - return first index of value. raises ValueError if the value is not present.
# .count()  - return number of occurrences of value.
# .sort()   - sort the list in ascending order and return None.
#           - the sort is in-place (i.e. the list itself is modified)
#           - and stable (i.e. the order of two equal elements is maintained).
# .reverse() - reverses the elements of the list (in-place)

numbers = [1, 2, 3, 4]

numbers.append(5) # [1, 2, 3, 4, 5]

numbers.extend([7, 8, 9, 11]) # [1, 2, 3, 4, 5, 7, 8, 9, 11]

numbers.insert(8, 10) # [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
numbers.insert(-1, 12) # [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 11]

last_item = numbers.pop() # 11
first_item = numbers.pop(0) # 1

numbers.remove(2)
# numbers.clear() # []

numbers.index(5)
numbers.index(7, 2)
numbers.index(8, 2, 10)

numbers.count(8) # 1

numbers.reverse() # [12, 10, 9, 8, 7, 5, 4, 3]

numbers.sort()

print(numbers)