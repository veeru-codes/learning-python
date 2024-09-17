# ask age
# age_str = input('Enter your age: ')

# if age_str:
#     age = int(age_str)
#     if age < 18:
#         print('Too young. Sorry!')
#     elif age >= 18 and age <= 21:
#         print('You can enter, but need a wristband')
#     elif age > 21:
#         print('You can drink')
# else:
#     print('Please enter an age!')


age_str = input('Enter your age: ')

if age_str:
    age = int(age_str)
    if age >= 21:
        print('Too young. Sorry!')
    elif age >= 18:
        print('You can enter, but need a wristband')
    else:
        print('You can drink')
else:
    print('Please enter an age!')