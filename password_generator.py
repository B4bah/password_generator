import random as rd

alphabet = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&*+,-./:;<=>?@\^_~'

length = int(input('Enter the password length:\n>>> '))
password = ''

for i in range(length):
    password += rd.choice(alphabet)

print(password)
