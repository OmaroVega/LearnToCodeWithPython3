inputed_number = input('Specify any number you want: ')
inputed_number = int(inputed_number)
print(inputed_number)

if inputed_number > 0:
    print('Inputed number: ' + str(inputed_number) + ' is bigger than 0')
elif inputed_number == 0:
    print('Inputed number: ' + str(inputed_number) + ' is equal to 0')
else:
    print('Inputed number: ' + str(inputed_number) + ' is smaller than 0')