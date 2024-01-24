hexNumbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}

# Converts a string Hexadecimal number into integer decimal
# If hexNum is not a valid hexadecimal number, returns None


# The number '1A' in hexadecimal would be 26 in decimal.
# Just like we have 'tens' place in base 10, hexadecimal has the 'sixteens'
# place. So '1A' would be 16 + 10 or 26


def hexToDec(hexCode):
    decCode = 0
    hexCodeLen = len(hexCode)
    i = 0

    while hexCodeLen >= 1:
        if hexCode[i] in hexNumbers:
            decCode += hexNumbers[hexCode[i]] * (16 ** (hexCodeLen - 1))
            hexCodeLen -= 1
            i += 1
        else:
            return None

    return decCode


# Pseudo code
# decCode <-- 0
# hexCodeLen <-- length of the hexCode str
# i <-- 0
# while the str length >= 1:
#   if the hexcode value exists in hexNumbers dictionary
#       calculate the decimal value of the hex and add it to the prev decCode (powers of 16)
#       decrease hexCodeLen by 1
#       decrease i by 1

print(hexToDec("A"))
print(hexToDec("0"))
print(hexToDec("1B"))
print(hexToDec("3C0"))
print(hexToDec("A6G"))
print(hexToDec("ZZTOP"))
