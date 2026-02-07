# handle errors with try-except-else-finally
# - try: code that may raise an error
# - except: code that runs if an error occurs in the try block
# - else: code that runs if no error occurs in the try block
# - finally: code that runs no matter what, even if an error occurs

def divide(a, b):
    try:
        result = a / b
    except TypeError as e:
        print("both arguments must be numbers")
        print(f"error details: {e}")
    except ZeroDivisionError:
        print("cannot divide by zero")
    else:
        print(f"result: {result}")
    finally:
        print("division operation complete")

divide(10, 2) # result: 5.0, division operation complete
divide(10, 0) # cannot divide by zero, division operation complete
divide(10, "a") # both arguments must be numbers, division operation complete

# guessing game example
import random
def guessing_game():
    number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("guess a number between 1 and 10: "))
        except ValueError:
            print("please enter a valid number")
            continue
        else:
            if guess == number:
                print("you guessed it!")
                break
            else:
                print("try again")
        finally:
            print("guessing game complete")

guessing_game()