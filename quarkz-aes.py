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

def modpow(x,n,m):
  if n == 0:
    return 1
  elif n == 1:
    return x
  elif n%2 == 0:
    return modpow(x*(x%m),n/2,m)%m
  elif n%2 == 1:
    return (x *  modpow(x*(x%m),(n-1)/2,m)%m )%m

decimal.getcontext().prec=100000

p = number.getPrime(1024)
q = number.getPrime(1024)
n = Decimal(p*q)
phi = Decimal((p-1)*(q-1))
#k = n
#
#ksize = sys.getsizeof(k)
#
#kb = int(k).to_bytes(ksize, "big")
#
#key = get_random_bytes(32)
#cipher = AES.new(key, AES.MODE_CTR)
#ct_bytes = cipher.encrypt(kb)
#o = int.from_bytes(ct_bytes, "big")

#o = Decimal(o) + Decimal(5.9)

# FIXES VULNERABILITY OF "o" BEING FACTORABLE AND EXPLOITED IN RSA.

#osize = len(bin(o))
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

d = Decimal(modInverse(int(e), int(phi)))

m = Decimal(98)

s = m**e

t = random.randint(1, 8000)



diff = abs(n-Decimal(o))

#print (diff)

if diff > 0:
    pub = n/diff
else:
    u = random.randint(0, 1000)
    o -= u
    diff = abs(n-o) % n
    pub = n/diff

#print ("pub: ", pub)
#print ("diff: ", diff)

count = Decimal(int(s)//int(o))

# print("count: ", count)

priv = round(((Decimal(count)%Decimal(pub))*diff)%n)

# print ("priv: ", priv)

#    print ("middle: ", count%pub)
#    print ("priv: ", priv)
c = modpow(m, e, o)

#    print ("c: ", c)

plain = pow((int(c)+int(priv)), int(d), int(n))
#print ("ciphertext: ", c)
#print ("message: ", s)
#print ("public key: ", o)
print ("plaintext: ", plain)
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

if plain != m and plain2 != m:
    print ("ERROR!!")
