animals = {"a": "aardvark", "b": "bear", "c": "cat"}

# Access the keys and values
print(animals["a"])

# Adding a new key
animals["d"] = "deer"
print(animals)

# updating the values
animals["a"] = "antelope"
print(animals)

print(animals.keys())
print(animals.values())

print(list(animals.keys()))

# if you try to access any key that not exists
# python will throw an error
# animals["e"]

print(animals.get("a"))

# we can also provide a default value to get()
print(animals.get("e", "elephant"))

animals2 = {"a": ["aardvark", "antelope"], "b": ["bear"]}

animals2["b"].append("bison")
print(animals2)

animals["c"] = ["cat"]
