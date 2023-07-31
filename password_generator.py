import random

alphabet = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&*+,-./:;<=>?@\^_~'

length = int(input('Enter the password length:\n>>> '))
password = ''

for i in range(length):
    password += random.choice(alphabet)

print(password)
