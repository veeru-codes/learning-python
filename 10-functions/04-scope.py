# scope
# - where our variables can be accessed!
# - variables created in functions are scoped in that function

# global
# - lets us reference variables that were originally assigned on the global scope

total = 0


def increment():
    global total
    total += 1
    return total


increment()  # 1


# nonlocal
# - lets us modify a parent's variables in a child (aka nested) function
# - you will not find yourself using the global or nonlocal keyword frequently
# - but it's essential to understand for scope!

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


print(outer())
