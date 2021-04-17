import math
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB)

def quark(base, sub, add):
    count = 0
    while base - sub > 0:
        base -= sub
        print (base)
        base += add
    print ('base: ', base)
    print ('count: ', count)
    return base

n = 13493
e = 49
d = 8389
m = 72

s = m**e

h = 23

#if h%1024 > 512:
#    h = h+512 

o = ((n**20)*100)^h
print (o)

t = (n*2)^h

#o = (n*8*9).to_bytes(16, 'big')

#print ((n*8*9), int.from_bytes(o, 'big'))

#o = int.from_bytes(cipher.encrypt(o), 'big')

y = (o%n)

c = math.floor(s / o)

x = s%o

a = quark(s, o, t)

#x = (x).to_bytes(16, 'big')

#x = int.from_bytes(cipher.decrypt(x), 'big')

print ("testing: ", (((a^h)**d)%n))
