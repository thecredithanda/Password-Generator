import random

char = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

long = input("Enter the number of passwords to be generated :")

long = int(long)

for p in range(long):

    length = input("Password Length :")

    length = int(length)

    password = ''

    for c in range(length):
        password += random.choice(char)

    print("Generated password is" )
    print(password)