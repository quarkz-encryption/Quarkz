from Crypto.Util import number
from decimal import Decimal
import decimal
from quarkz.dtypes import KeyPair
import random
import sys
import binascii


decimal.getcontext().prec=100000

def gcd(a, b): 
   while a != 0:
      a, b = b % a, a
   return b

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def modpow(x,n,m):
  if n == 0:
    return 1
  elif n == 1:
    return x
  elif n%2 == 0:
    return modpow(x*(x%m),n/2,m)%m
  elif n%2 == 1:
    return (x *  modpow(x*(x%m),(n-1)/2,m)%m )%m

def convert_to_int(data: str) -> int: 
    return int.from_bytes(data.encode(), 'big')

def convert_to_str(data: int) -> str:
    return data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()

    



def createKey(keysize: int = 1024):
    p = number.getPrime(keysize)
    q = number.getPrime(keysize)
    n = Decimal(p*q)
    #print(n)
    phi = Decimal((p-1)*(q-1))
    while True:
        e = Decimal(number.getPrime(8))
        r = gcd(int(e), int(phi))
        if r == 1:
            t = Decimal(random.getrandbits(4))
            o = e**t
            break

    d = Decimal(mod_inverse(int(e), int(phi)))

    #print ("osize: ", sys.getsizeof(o)*8)
    
    diff = (abs(n-Decimal(o))) % n

    #print(n)

    x = Decimal(random.getrandbits(8192))

    if diff > 0:
        ratio = (n/diff) * x
        #print ("ratio: ", sys.getsizeof(round(ratio))*8)
    else:
        u = random.randint(0, 1000)
        o -= u
        diff = abs(n-o) % n
        ratio = (n/diff) * x

    privateKey = {
        "d": d,
        "n": n,
        "diff": diff,
        "r": (n/diff),
    }

    publicKey = {
        "e": e,
        "o": o,
        "ratio": ratio,
        "diff": diff,
        "x": x,
        "n": n
    }

    keyPair = {
        "private_key": privateKey,
        "public_key": publicKey
    }

    return KeyPair(**keyPair)
