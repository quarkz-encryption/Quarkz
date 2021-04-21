n = 8549
e = 511
d = 1735
m = 71
s = m**e

h = 87

o = (n*8*4*7)^h

t = n*432

for i in range(0, 1000):
    x = (s%n)+(o*(2**i))
    a = ((x^(h*(2**i)))**d)%n
    if a == m:
        print ("index: ", (2**i), i)
        print ("ciphertext: ", bin(x))
        print ("initial: ", bin(s%n))
        print ("key: ", bin(h))
        print ("variable: ", bin(o))
