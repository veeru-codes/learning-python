# an ordered collection of grouping of items
# it is immutable - can never be changed

alphabet = ('a', 'b', 'c', 'd')
print(alphabet)

# this gives an error:
# -- tuple object has no attribute 'append'
# -- tuple object does not support item assignment
# alphabet.append('e')
# alphabet[0] = 'A'

# why use a tuple?
# -- tuples are faster than lists
# -- it makes your code safer
# -- valid keys in a dictionary

# tuples are commonly used for unchanging data
months = (
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
)

# we can use tuples as keys in dictionaries
locations = {
    (35.6895, 39.6917): 'tokyo office',
    (40.7128, 74.0060): 'new york office',
    (37.7749, 122.4194): 'san fransisco office'
}

# looping tuples
for month in months:
    print(month)

i = len(months) - 1
while i >= 0:
    print(months[i])
    i = i - 1

# methods
# -- count - returns the number of times a value appears in a tuple
# -- index - returns the index at which a value found in a tuple
print(months.count('january'))
print(months.index('january'))
