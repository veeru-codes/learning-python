# *args
# a special operator we can pass to functions
# gathers remaining arguments as a tuple
# this is just a parameter - you can call it whatever you want!

def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15


def ensure_correct_info(*args):
    if "colt" in args and "steele" in args:
        return "welcome back colt!"
    return "not sure who you are..."


print(ensure_correct_info(1, True, "colt", "steele"))
