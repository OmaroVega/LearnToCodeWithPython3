# Python Program - Remove vowels from specified string

def remove_vowels(newStr,string):
    vowels = ('a','e','i','o','u')
    for c in string.lower():
        if c in vowels:
            newStr = newStr.replace(c,'')
    return newStr
print('Introduce x para salir.')
string = input('Introduce cualquier string a la que elmininar las vocales: ')

if string == 'x':
    exit()
else:
    newStr = string
    print('Eliminando las vocales de la string indicada...')
    newStr = remove_vowels(newStr,string)
    print('La nueva string despues de la eliminación de vocales es: ' + newStr)