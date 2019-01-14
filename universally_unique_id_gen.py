
import string
from random import randrange

import calendar
from datetime import datetime

def uuid_gen():

    id_lenght = 36
    alphabet = '0123456789abcdef'
    
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    timestamp_hex = hex(unixtime).split('x')[1]
    print(timestamp_hex)

    id_list = []

    for i in range(id_lenght):
        if i in [8-8,13-8,18-8,23-8]:
            id_list.append('-')
        else:
            index = randrange(len(alphabet))
            id_list.append(alphabet[index])

    id = timestamp_hex + ''.join(id_list)    
    return id


print('-------------')

UUID = uuid_gen()
print(f'->> Random UUID : {UUID}')