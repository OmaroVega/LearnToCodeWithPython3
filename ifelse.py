password = "Password.123"

input_password = input("Please enter the password: ")
input_password = str(input_password)

if input_password == password:
    print("Correct Password!")
    print("Access Granted!")
else:
    print("Wrong Password!")
    print("Access Deniend!")
    