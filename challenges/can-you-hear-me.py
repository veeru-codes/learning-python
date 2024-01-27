import random
import time

servicesAreUp = True


def getData50():
    if servicesAreUp and random.random() < 0.5:
        return "You got the data! That only happens 50% of the time"


def getData25():
    if servicesAreUp and random.random() < 0.25:
        return "You got the data! That only happens 25% of the time"


def getData10():
    if servicesAreUp and random.random() < 0.1:
        return "You got the data! That only happens 10% of the time"


def getWithRetry(dataFunc):
    response = ""
    for i in range(30):
        response = dataFunc()
        if response:
            return response


data1 = getWithRetry(getData50)
print(data1)

data2 = getWithRetry(getData25)
print(data2)

data3 = getWithRetry(getData10)
print(data3)

servicesAreUp = False

data4 = getWithRetry(getData50)
print(data4)

data5 = getWithRetry(getData25)
print(data5)

data6 = getWithRetry(getData10)
print(data6)
