import random
n = 187
e = 3
d = 107
m = 72
s = m**e

h = 31

k = n*34

j = n*17

o = (n*34)^h

c = s+h

for i in range (1, 1000): 
    rand = random.randint(1, i)
    left = i - rand
    ik = k*rand 
    ij = j*left
    cipher = c + ik + ij
    
    if (cipher^h)%n == 183:
        print ("index: ", i)
        print ("cipher: ", bin(cipher))
        print ("undone: ", bin(cipher^h))
