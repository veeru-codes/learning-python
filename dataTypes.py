from decimal import Decimal, getcontext

integerNum = 10
floatingNum = 2.34


print(int(2.34))
print(int(8.999999999))
print(int("abcdef", 16))
print(float(16))
print(float(20))

print(bool(0))
print(bool(1))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool("True"))
print(bool("False"))
print(bool("Apple"))
print(bool(True))
print(bool(False))

name = "Veerendra"
age = 20
print(f"My name is {name} and my age is {age}")

multilineString = """
Here is a long block of text
I can add new lines!
The text doesn't stop until it sees \'\'\'
"""

print(bytes(4))
print(bytes("💕", "utf-8"))
