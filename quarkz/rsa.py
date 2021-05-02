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

def encrypt(message: int) -> tuple: 
    p = number.getPrime(1024)
    q = number.getPrime(1024)
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

    assert(type(message) == int)

    m = Decimal(message) 
    s = m**e
    t = random.randint(1, 8000)
    
    diff = abs(n-Decimal(o))


    if diff > 0:
        pub = n/diff
    else:
        u = random.randint(0, 1000)
        o -= u
        diff = abs(n-o) % n
        pub = n/diff

    count = Decimal(int(s)//int(o))

    priv = round(((Decimal(count) % Decimal(pub)) * diff) % n)

    data = {"e": e, "m": m, "o": o, "priv": priv, "pub": pub, "d": d, "n": n}
    return Encrypted(**data) 


def decrypt(encrypted: quarkz.dtypes.Encrypted) -> str:
    c = utils.modpow(encrypted._m, encrypted._e, encrypted._o)
    plain = pow((int(c)+int(encrypted._priv)), int(encrypted._d), int(encrypted._n))
    
    if plain: 
        return plain
    else: 
        return pow((int(c)-int(encrypted._priv)), int(encrypted._d), int(encrypted._n))



if __name__ == "__main__":
    args = encrypt(98)

    print(decrypt(**args))



















