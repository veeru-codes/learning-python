myList = [1, 2, 3, 4, 5, 6]

# Slicing -- [start:end(not included):step]
print(myList[:])
print(myList[0:4])
print(myList[1:])
print(myList[::2])
print(myList[1::2])
print(myList[::-1])

myList.append(7)
print(myList)
myList.insert(3, "a new value")
print(myList)
print(myList.pop())
len(myList)
myList.remove(4)
print(myList)
