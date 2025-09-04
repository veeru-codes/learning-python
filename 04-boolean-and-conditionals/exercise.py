# bouncer
age = input('enter age: ')
if age:
    age = int(age)
    if 18 <= age < 21:
        print('you can enter, but need a wristband!')
    elif age >= 21:
        print('you are good to enter and can drink!')
    else:
        print('you cannot come in, little one!')
else:
    print('please enter a valid age')

