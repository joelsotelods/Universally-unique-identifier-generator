
import string
import calendar
from datetime import datetime
from random import randrange

## Function to generate random UUIDs
def uuid_gen():
    
    # Lenght is 36 (32 Hexadecimal characters and 4 hyphens)
    id_lenght = 36
    alphabet = '0123456789abcdef'
    
    # Getting the timestamp in hex-- used for the first 8 chars on the UUID key
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    timestamp_hex = hex(unixtime).split('x')[1]
    #print(timestamp_hex)

    id_lenght -= len(timestamp_hex)

    id_list = []

    #generate a list of random hex characters
    for i in range(id_lenght):
        # conditional to add hyphens on the UUID code
        if i in [0,5,10,15]:
            id_list.append('-')
        else:
            index = randrange(len(alphabet))
            id_list.append(alphabet[index])

    #concatenate the timestamp to the randomly generated key
    id = timestamp_hex + ''.join(id_list)    
    return id


## calling the function to generate generate and print the Key.
UUID = uuid_gen()
print(f'Random UUID : {UUID}')
print(f'Lenght: {len(UUID)}')