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

def gcd(a, b): 
   while a != 0:
      a, b = b % a, a
   return b

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

decimal.getcontext().prec=10000

p = number.getPrime(2048)
q = number.getPrime(2048)
n = Decimal(p*q)
phi = Decimal((p-1)*(q-1))

while True:
    e = Decimal(number.getPrime(11))
    r = gcd(int(e), int(phi))
    if r == 1:
        break

d = Decimal(modInverse(int(e), int(phi)))

m = Decimal(27)

s = m**e

k = n

ksize = sys.getsizeof(k)

kb = int(k).to_bytes(ksize, "big")

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(kb)
o = int.from_bytes(ct_bytes, "big")
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

#o = k^t

diff = abs(k-Decimal(o)) % n

#print (diff)

if diff > 0:
    pub = n/diff
else:
    u = random.randint(0, 1000)
    o -= u
    diff = abs(k-o) % n
    pub = n/diff

count = Decimal(int(s)//int(o))

priv = round((Decimal(count)%Decimal(pub))*diff)

c = pow(m, e, o)

plain = pow((int(c)+int(priv)), int(d), int(n))
print ("ciphertext: ", c)
print ("message mod e: ", s)
print ("public key aes encrypted: ", o)
print ("plaintext returned: ", plain)
plain2 = pow((int(c)-int(priv)), int(d), int(n))

#    if plain == m:
#
#        print("index: ", i)
#        print("something cool: ", (count%pub)*diff)
#        #print ("plain: ", plain)
#        #print ("cipher: ", c)
#        #print ("s: ", s)
#        #print ("k: ", k)
#        #print ("o: ", o)
#        #print ("diff: ", diff)
#        #print ("pub: ", pub)
#        #print ("count: ", count)
#        #print ("priv: ", priv)
#
#    
#    elif plain2 == m:
#
#        print ("==========================================")
#        print("index: ", i)
#        print("something cool: ", (count%pub)*diff)
#        print ("plain: ", plain2)
#        print ("cipher: ", c)
#        print ("s: ", s)
#        print ("k: ", k)
#        print ("o: ", o)
#        print ("diff: ", diff)
#        print ("pub: ", pub)
#        print ("count: ", count)
#        print ("priv: ", priv)
#        print ("*******************************************8")

if plain != m:
    print ("ERROR!!")
