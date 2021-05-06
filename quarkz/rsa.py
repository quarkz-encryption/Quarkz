import random
import sys
import json
import decimal

from base64 import b64encode, b64decode
from decimal import Decimal

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import number
from Crypto.PublicKey import RSA 

from quarkz import utils 
from quarkz.dtypes import Encrypted 
import quarkz

decimal.getcontext().prec=100000


def encrypt(message: int, publicKey: dict) -> quarkz.dtypes.Encrypted: 

    assert(type(message) == int)

    m = Decimal(message)
    s = m**publicKey["e"]

    count = Decimal(int(s) // int(publicKey["o"]))

    print("count: ", sys.getsizeof(count) * 8)

    offsetCount = Decimal(count) % Decimal(publicKey["ratio"])

    n1 = (publicKey["ratio"] * publicKey["o"]) / (publicKey["ratio"] - 1)

    d = n1 / publicKey["ratio"]

    n2 = d + publicKey["o"]

    print (round(n1))
    print (round(n2))

    #print (round(publicKey["ratio"]))

    print("offset: ", sys.getsizeof(round(offsetCount))*8)

    ciphertext = Decimal(pow(m, publicKey["e"], publicKey["o"])) #might need to change back to modpow func

    print ("ciphertext generated: ", ciphertext)

    data = {"ciphertext": ciphertext, "offsetCount": offsetCount}

    return Encrypted(**data)


def decrypt(encrypted: quarkz.dtypes.Encrypted, keypair: quarkz.dtypes.KeyPair) -> int:
    encrypted = vars(encrypted)

    privateKey = keypair.get_private_key()

    offset = (round(((encrypted["offset"] % privateKey["r"]) * privateKey["diff"]))) % (privateKey["n"])

    ciphertext = int(encrypted["ciphertext"] - offset)

    plaintext = pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))

    print (plaintext)
    
    if plaintext:
        return plaintext
    else: 
        ciphertext = int(encrypted["ciphertext"] + offset)
        return pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))



if __name__ == "__main__":
    #first, create a new key pair 
    pair = utils.createKey(1024)

    #encrypt some data
    message = 69
    public_key = pair.get_public_key()
    encrypted_data = encrypt(message, public_key)

    #decrypt the data again
    decrypted_data = decrypt(encrypted_data, pair)
    print(decrypted_data)
