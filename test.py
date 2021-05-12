from quarkz.utils import createKey

import random
import time

key_pair = createKey(keysize=8092)

from quarkz.rsa import encrypt

pub_key = key_pair.get_public_key()

start = time.time()

datasize = 0

some_data = random.getrandbits(256)

print ("plaintext encrypted: ", some_data)

encrypted_data = encrypt(some_data, pub_key)

datasize += 256

end = time.time()

from quarkz.rsa import decrypt

decryptsize = 0

start = time.time()

decrypted_data = decrypt(encrypted_data, key_pair)
decryptsize += 256

end = time.time()

print("plaintext returned: ", decrypted_data) 
