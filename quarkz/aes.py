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

decimal.getcontext().prec=100000

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

m = Decimal(98)

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


priv = round(((Decimal(count)%Decimal(pub))*diff)%n)

c = utils.modpow(m, e, o)


plain = pow((int(c)+int(priv)), int(d), int(n))

print ("plaintext: ", plain)
plain2 = pow((int(c)-int(priv)), int(d), int(n))

if plain != m and plain2 != m:
    print ("ERROR!!")
