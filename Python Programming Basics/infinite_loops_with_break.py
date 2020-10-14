password = 'arcoiris'

while True:

    inputed_password = input('Introduzca la contraseña: ')
    inputed_password = str(inputed_password)

    if inputed_password == password:
        break

print('Contraseña correcta')
print('Acceso concedido')
