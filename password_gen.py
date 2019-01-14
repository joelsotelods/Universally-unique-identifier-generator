
import string
from random import randrange


def password_gen(id_lenght = 7, alphabet = string.ascii_letters + string.digits):

    id_list = []

    for i in range(id_lenght):
        index = randrange(len(alphabet))
        id_list.append(alphabet[index])

    id = ''.join(id_list)    

    #timesta
    return id


print('-------------')
passwrd = password_gen()
print(f'->> Password with default function: {passwrd}')

print('-------------')
lenght = 15
passwrd = password_gen(lenght)
print(f'->> Password with function with lenght of {lenght}: {passwrd}')

print('-------------')
alpha = 'xyz-654'
passwrd = password_gen(alphabet = alpha)
print(f'->> Password with function with an Alphabet = "{alpha}": {passwrd}')

print('-------------')
lenght = 40
alpha = 'abxy01'
passwrd = password_gen(lenght,alpha)
print(f'->> Password with function with lenght of {lenght} and an Alphabet = "{alpha}": {passwrd}')
