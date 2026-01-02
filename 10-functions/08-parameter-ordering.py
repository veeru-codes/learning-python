# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor="veera", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="reddy", job="instructor"))

# [1, 2, (3,), 'veera', {'last_name': 'reddy', 'job': 'instructor'}]
