import random

def guess_number():
    
    global guess

    for i in range(1,4):
        print('Intenta adivinar el número')
        guess = int(input('Introduce un número entre 1 y 20: '))

        if guess < secretNumber:
            print('El número introducido es inferior')
        elif guess > secretNumber:
            print('El número introducido es mayor')
        elif guess == secretNumber:
            break
    

def check(guess, secretNumber):
    if guess == secretNumber:
        print('Felicidades, has adivinado el número')
    else:
        print('Inténtelo la próxima vez, el número correcto era: ' + str(secretNumber))

secretNumber = random.randint(1,20)
print('Estoy pensando en un número.')

guess_number()
check(guess,secretNumber)

