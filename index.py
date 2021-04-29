n = 8549
e = 511
d = 1735
m = 112
s = m**e

h = 87

j = 82

o = (n*8*4*7)^h

t = (n*(786))

# Modulo

#for i in range(0, 1000):
#
#    q = ((s)//(o*(2**i)))
#
#    p = ((2**i)*q)-4
#
#    x = (((s%t))%(o*(2**i)))^p
#    x = (~(x-1))
#    a = ((x^(h*(2**i)))**d)%n
#    if True:
#        print ("index: ", (2**i), i)
#        print ("p: ", bin(p))
#        print ("ciphertext: ", bin(x))
#        print ("initial: ", bin((s)))
#        print ("aes decrypt: ", bin(x^(h*(2**i))))
#        print ("key: ", bin(h))
#        print ("variable: ", bin(o))
#        print ("=======================================================================================================================================")

# Subtraction

#for i in range(1, 1000):
#
#    p = ((2**(i)))-4
#
#    x = (((s%t))-(o*(2**i)))^p
#    x = (~(x-1))
#    a = ((x^(h*(2**i)))**d)%n
#    if True:
#        print ("index: ", (2**i), i)
#        print ("p: ", bin(p))
#        print ("variable: ", bin(o))
#        print ("ciphertext: ", bin(x))
#        print ("initial: ", bin((s%t)))
#        print ("aes decrypt: ", bin(x^(h*(2**i))))
#        print ("key: ", bin(h))
#        print ("=======================================================================================================================================")

# Addition

for i in range(0, 1000):
    x = ((s%t))+(o*(2**i))
    a = ((x^(h*(2**i)))**d)%n
    if a == m:
        print ("index: ", (2**i), i)
        print ("variable: ", bin(o))
        print ("ciphertext: ", bin(x))
        print ("initial: ", bin((s%n)+t))
        print ("aes decrypt: ", bin(x^(h*(2**i))))
        print ("key: ", bin(h))
        print ("=======================================================================================================================================")
