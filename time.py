from quarkz.utils import createKey 
from quarkz.rsa import encrypt, decrypt
from decimal import Decimal
import time, sys, decimal

decimal.getcontext().prec=5000

if __name__ == "__main__":
    createtime = []
    encrypttime = []
    decrypttime = []
    #message = input('enter text: ')
    message = "testing"
    print ("message size: ", sys.getsizeof(message))
    #for i in range(1, 10001):
    for i in range(0, 100):
        start = time.time()
        key = createKey(keysize=256)
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

    print(f'end message: {decrypted_data}!')
    ctime = Decimal(sum(createtime) / len(createtime))
    etime = Decimal(sum(encrypttime) / len(encrypttime))
    dtime = Decimal(sum(decrypttime) / len(decrypttime))
    ttime = ctime + etime + dtime
    print ("create key time: ", (ctime))
    print ("encrypt time: ", (etime))
    print ("decrypt time: ", (dtime))
    print ("total: ", ttime)
