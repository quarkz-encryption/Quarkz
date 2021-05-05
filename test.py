from quarkz.utils import createKey

import random

from timeit import default_timer

create = default_timer()

key_pair = createKey(keysize=129)

#print(default_timer() - create)
#print(key_pair) 

from quarkz.rsa import encrypt

start = default_timer()

pub_key = key_pair.get_public_key()

some_data = random.getrandbits(128)

print ("plaintext to encrypt: ", some_data)

encrypted_data = encrypt(some_data, pub_key)

#print(encrypted_data) 

from quarkz.rsa import decrypt

decrypted_data = decrypt(encrypted_data, key_pair)

print("plaintext returned: ", decrypted_data) 
#print(default_timer() - start)