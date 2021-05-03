from Crypto.Util import number
from decimal import Decimal
from quarkz.dtypes import KeyPair
import random

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

def createKey(keysize: int = 1024):
    p = number.getPrime(keysize)
    q = number.getPrime(keysize)
    n = Decimal(p*q)
    phi = Decimal((p-1)*(q-1))
    while True:
        e = Decimal(number.getPrime(10))
        r = gcd(int(e), int(phi))
        if r == 1:
            break
    while True:
        j = random.randint(1000, 10000)
        o = (e-1)**j
        check = gcd(int(e), int(o-1))
        if check != 1:
            break

    d = Decimal(mod_inverse(int(e), int(phi)))
    
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
        "private_key": privateKey,
        "public_key": publicKey
    }

    return KeyPair(**keyPair)