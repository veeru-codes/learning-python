# milage converter
import math

no_of_kms = int(input('how many kilometers did you run today? '))
no_of_miles = no_of_kms * 0.621371
print(f"your {no_of_kms}kms is {round(no_of_miles, 2)}mi")
