# Universally Unique Identifier (UUID) generator.

A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems.

For reference: [Universally Unique Identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier)


### Code:

Importing Libraries:

```python
import string
import calendar
from datetime import datetime
from random import randrange
```

Declaring the function:

```python
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
```

Calling the function to get the Random UUID:

```python

## calling the function to generate generate and print the Key.
UUID = uuid_gen()
print(f'Random UUID : {UUID}')
print(f'Lenght: {len(UUID)}')

```

### Output

```shell
Terminal$ python3 universally_unique_id_gen.py 
Random UUID : 5c3ce67c-f3fa-5d15-b6a3-9d7a6e5e72ce
Lenght: 36
```
