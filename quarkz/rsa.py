import random
import sys
import json
import decimal
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import number
from Crypto.PublicKey import RSA 
from decimal import Decimal
from quarkz import utils 
from quarkz.dtypes import Encrypted
import quarkz

decimal.getcontext().prec=100000

def createKey(keySize: int):
    p = number.getPrime(keySize)
    q = number.getPrime(keySize)
    n = Decimal(p*q)
    phi = Decimal((p-1)*(q-1))
    while True:
        e = Decimal(number.getPrime(10))
        r = utils.gcd(int(e), int(phi))
        if r == 1:
            break
    while True:
        j = random.randint(1000, 10000)
        o = (e-1)**j
        check = utils.gcd(int(e), int(o-1))
        if check != 1:
            break

    d = Decimal(utils.mod_inverse(int(e), int(phi)))
    
    diff = abs(n-Decimal(o))


    if diff > 0:
        ratio = n/diff
    else:
        u = random.randint(0, 1000)
        o -= u
        diff = abs(n-o) % n
        ratio = n/diff

    privateKey = {
        "d": d,
        "n": n,
        "diff": diff,
    }

    publicKey = {
        "e": e,
        "o": o,
        "ratio": ratio
    }

    keyPair = {
        "privateKey": privateKey,
        "publicKey": publicKey
    }

    return keyPair

def encrypt(message: int, publicKey: dict) -> tuple: 

    assert(type(message) == int)

    m = Decimal(message)
    s = m**publicKey["e"]

    count = Decimal(int(s) // int(publicKey["o"]))

    offsetCount = Decimal(count) % Decimal(publicKey["ratio"])

    ciphertext = Decimal(pow(m, publicKey["e"], publicKey["o"])) #might need to change back to modpow func

    data = {"ciphertext": ciphertext, "offsetCount": offsetCount}

    return data


def decrypt(encrypted: dict, privateKey: dict) -> int:
    
    offset = (round(encrypted["offsetCount"] * privateKey["diff"])) % privateKey["n"]

    ciphertext = int(encrypted["ciphertext"] + offset)

    plaintext = pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))
    
    if plaintext:
        return plaintext
    else: 
        ciphertext = int(encrypted["ciphertext"] - offset)
        return pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))



if __name__ == "__main__":
    args = encrypt(98)

    print(decrypt(**args))
