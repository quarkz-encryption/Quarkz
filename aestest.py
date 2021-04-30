import random
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import decimal
from decimal import Decimal

decimal.getcontext().prec=1000

n = Decimal(799133)
e = Decimal(101)
d = Decimal(710501)
m = Decimal(73)

s = m**e

t = random.randint(1, 8000)

for i in range(2, 100000):

    k = n*Decimal(i)

    kb = int(k).to_bytes(16, "big")

    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(kb)
    o = int.from_bytes(ct_bytes, "big")
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
#    result = json.dumps({'nonce':nonce, 'ciphertext':ct})

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

#    print ("pub: ", pub)
#    print ("diff: ", diff)

    count = Decimal(int(s)//int(o))

#    print("count: ", count)

    priv = round((Decimal(count)%Decimal(pub))*diff)

#    print ("middle: ", count%pub)
#    print ("priv: ", priv)
    c = pow(m, e, o)

#    print ("c: ", c)

    plain = pow((int(c)+int(priv)), int(d), int(n))
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
