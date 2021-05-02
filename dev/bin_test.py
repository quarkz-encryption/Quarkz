import math
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB)

def quark(base, add, sub):
    count = 0
    c = 0
    while base + add < 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        base += add
        count += 1
        c += 1
        if c % 4 == 0:
            base -= sub
            count -= 1 
        print ("base: ", base)
        print ("count: ", count)
        if count == 32:
            return base
            break
    return base

n = 13493
e = 49
d = 8389
m = 72

s = m**e

h = 23

o = (n*6*9)^h

t = (n*2*45)^h

print ("o: ", o)

y = (o%n)

c = math.floor(s / o)

x = s%o

print ("s: ", s)

a = quark(s, o, t)

#x = (x).to_bytes(16, 'big')

#x = int.from_bytes(cipher.decrypt(x), 'big')

print ("testing: ", (((a^(h*32))**d)%n))
