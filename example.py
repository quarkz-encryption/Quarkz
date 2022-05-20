from quarkz.utils import createKey 
from quarkz.quarkz import encrypt, decrypt
from decimal import Decimal
import time, sys, decimal

decimal.getcontext().prec=5000

if __name__ == "__main__":
    createtime = []
    encrypttime = []
    decrypttime = []
    #message = input('enter text: ')
    message = input("This is a test: ")
    print ("message to be encrypted: ", message)
    start = time.time()
    key = createKey(keysize=512)
    pub = key.get_public_key()
    end = time.time()
    createtime.append(end-start) 
    
    start = time.time()
    encrypted_data = encrypt(message, pub)
    end = time.time()
    encrypttime.append(end-start) 

    start = time.time()
    decrypted_data = decrypt(encrypted_data, key) 
    end = time.time()
    decrypttime.append(end-start)

    print ("decrypted data: ", decrypted_data)
