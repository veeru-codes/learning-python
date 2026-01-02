# **kwargs
# a special operator we can pass to functions
# gathers remaining keyword arguments as a dictionary
# this is just a parameter -- you can call it whatever you want!

def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f'{person}: {color}')


fav_colors(veera='red', ruby="red", ethel="teal")
fav_colors(veera='red', ruby="red", ethel="teal", ted="blue")


def special_greeting(**kwargs):
    if "david" in kwargs and kwargs["david"] == "special":
        return "you get a special greeting david!"
    elif "david" in kwargs:
        return f"{kwargs['david']} david!"

    return "not sure who this is..."


print(special_greeting(heather="hello", david="special"))
