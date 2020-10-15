# Python Program - Simple Python Calculator

def add(num1,num2):
    result = num1 + num2
    print('El resultado es: ' + str(result))

def subs(num1,num2):
    result = num1 - num2
    print('El resultado es: ' + str(result))

def mul(num1,num2):
    result = num1 * num2
    print('El resultado es: ' + str(result))

def div(num1,num2):
    result = num1 / num2
    print('El resultado es: ' + str(result))

print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. Salir')

while True:
    choice = int(input('Introduce tu elección: '))
    if choice >= 1 and choice <=4:
        print('Introduce dos números')
        num1 = int(input('Introduce el primer número: '))
        num2 = int(input('Introduce el segundo número: '))
        if choice == 1:
            add(num1,num2)
        elif choice == 2:
            subs(num1,num2)
        elif choice == 3:
            mul(num1,num2)
        else:
            div(num1,num2)
    elif choice == 5:
        break
    else:
        print('Has introducido un número incorrecto.')