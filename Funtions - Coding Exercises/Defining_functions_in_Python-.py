import random

def getNumber(number):
    if number == 1:
        return 'El número es 1'
    elif number == 2:
        return 'El número es 2'
    elif number == 3:
        return 'El número es 3'
    elif number == 4:
        return 'El número es 4'
    elif number == 5:
        return 'El número es 5'

random_number = random.randint(1,5)
pick = getNumber(random_number)
print(pick)