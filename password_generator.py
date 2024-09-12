import random
import os

title = input('Enter the title for the password:\n>>> ')

alphabet = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&*+,-./:;<=>?@_~'

length = int(input('Enter the password length:\n>>> '))
password = ''

for i in range(length):
    password += random.choice(alphabet)

with open(f'C:/Files/Main Passwords/{title}.txt', 'w') as file:
    file.write(password)

os.startfile(f'C:/Files/Main Passwords/{title}.txt')