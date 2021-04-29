n = 187
e = 3
d = 107
m = 72

s = m**e

t = 574

k = n*23

o = k^t

diff = abs(k-o)

pub = n/diff

count = s//o 

priv = round((count%pub)*diff)

cipher = s%o

plain = (((cipher+priv)**d)%n)

print (plain)
