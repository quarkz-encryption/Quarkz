import random
from Crypto.Util import number
from Crypto.PublicKey import RSA

x = random.randint(4, 8)
p = number.getPrime(x)
x = random.randint(4, 8)
q = number.getPrime(x)


def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return (1)

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

n = (p*q)
while True:
    x = random.randint(4, 8)
    e = number.getPrime(x)
    r = gcd(e, n)
    if r == 1:
        break
d = modInverse(e, (p-1) * (q-1))
cipher = []
word = []
word_full = []
m = input("enter text: ") # raw_input for python 2

print ("THIS IS E: " + str(e))

rounds = random.randint(20, 200)

for i in m:
    mc = (ord(i)**e)
    for k in range(1, rounds):
        ocheck = random.randint(1,2)
        if ocheck == 1:
            oit = random.randint(20, 20000)
            o = (n * oit)
        else:
            oit = random.randint(20, 50)
            o = (n ** oit)
    for j in range(1, rounds):
        tcheck = random.randint(1,2)
        if tcheck == 1:
            tit = random.randint(20, 20000)
            t = (n * tit)
        else:
            tit = random.randint(20, 50)
            t = (n ** tit)
    ox = o + 1
    tx = t + 1
    print ("THIS IS O (GENERATED FROM N) FOR THE BELOW CIPHERTEXT: " + str(o))
    print ("THIS IS T (GENERATED FROM N) FOR THE BELOW CIPHERTEXT: "+ str(t))
    check = random.randint(1,2)
    rounds_user = random.randint(100, 1000)
    c = mc
    for b in range(1, rounds_user):
        mult_check = random.randint(1,2)
        if check == 1:
            if mult_check == 1:
                c = (c * ox)
            else:
                c = (c * tx)
        else:
            if mult_check == 1:
                c = (c + o)
            else:
                c = (c + t)
    c = (c % o) 
#    print (c / 29)
    print ("Cipher Text of " + i + ": " + str(c))
    cipher.append(c)
    #print (c % n)
    #print (mc % n)
    cf = (c % n)
    plain = ((cf**d)%n)
    word.append(plain)

for y in word:
    word_full.append(str(chr(y))) # unichr for python 2

plaintext = ''.join(word_full)

print ("Return: " + plaintext)
