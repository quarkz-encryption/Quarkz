import random
from decimal import Decimal
import decimal

decimal.getcontext().prec=10000

n = 589
e = 47
d = 23
m = 104

s = m**e

t = random.randint(1, 8000)

for i in range(2, 10000):

    k = n*i

    o = k^t

    diff = abs(k-o) % n

    pub = n/diff

    count = s//o 

    with decimal.localcontext() as ctx:
        ctx.prec = len(Decimal(count).as_tuple().digits) + 2

    priv = round((Decimal(count)%Decimal(pub))*diff)
    print (priv)

    cipher = s%o

    plain = (((cipher+priv)**d)%n)
    plain2 = (((cipher-priv)**d)%n)

    if plain == m:

        print("index: ", i)
        print("something cool: ", (count%pub)*diff)
        #print ("plain: ", plain)
        #print ("cipher: ", cipher)
        #print ("s: ", s)
        #print ("k: ", k)
        #print ("o: ", o)
        #print ("diff: ", diff)
        #print ("pub: ", pub)
        #print ("count: ", count)
        #print ("priv: ", priv)

    
    elif plain2 == m:

        print ("==========================================")
        print("index: ", i)
        print("something cool: ", (count%pub)*diff)
        print ("plain2: ", plain2)
        print ("cipher: ", cipher)
        print ("s: ", s)
        print ("k: ", k)
        print ("o: ", o)
        print ("diff: ", diff)
        print ("pub: ", pub)
        print ("count: ", count)
        print ("priv: ", priv)
        print ("*******************************************8")

    else:
        print ("ERROR!!")
        print ("plain2: ", plain2)
        print ("plain: ", plain)
