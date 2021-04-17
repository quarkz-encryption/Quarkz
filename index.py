n = 13493
e = 49
d = 8389
m = 72
s = m**e

h = 27

o = (n*7*6)^h


for i in range(1, 1000):
    x = s+(o*i)
    a = ((x^(h*i))**d)%n
    if a == m:
        print (i)
