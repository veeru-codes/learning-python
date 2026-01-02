def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total


nums = [1, 2, 3, 4, 5]
print(sum_all(*nums))  # 15
