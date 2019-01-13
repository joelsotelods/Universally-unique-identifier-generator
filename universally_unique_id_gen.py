
import string
from random import randrange

def uuid(id_lenght = 4, alphabet = string.ascii_letters + string.digits):

    id_list = []

    for i in range(id_lenght):
        index = randrange(len(alphabet))
        id_list.append(alphabet[index])

    id = ''.join(id_list)    
    return id

print('-------------')
UUID = uuid()
print(f'->> Default function: {UUID}')
print('-------------')
lenght = 15
UUID = uuid(lenght)
print(f'->> Function with lenght of {lenght}: {UUID}')
print('-------------')
alpha = 'xyz-654'
UUID = uuid(alphabet = alpha)
print(f'->> Function with an Alphabet = "{alpha}": {UUID}')
print('-------------')
lenght = 40
alpha = 'abxy01'
UUID = uuid(lenght,alpha)
print(f'->> Function with lenght of {lenght} and an Alphabet = "{alpha}": {UUID}')

