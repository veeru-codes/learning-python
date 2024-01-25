myList = [1, 2, 3, 4, 5, 6]

# [(condition) (for loop syntax)]
doubles = [2 * item for item in myList]
print(doubles)

# List comprehensions with filters
evenNums = [item for item in myList if item % 2 == 0]
print(evenNums)

oddNums = [item for item in myList if item % 2 != 0]
print(oddNums)

# List comprehensions with functions
myString = "My name is Veerendra. I live in Kent"


def cleanWord(word):
    return word.replace(".", "").lower()


cleanWords = [cleanWord(word) for word in myString.split(" ")]
print(cleanWords)

# Nested list comprehensions
listOfCleanWords = [
    [cleanWord(word) for word in sentence.split()] for sentence in myString.split(".")
]

print(listOfCleanWords)
