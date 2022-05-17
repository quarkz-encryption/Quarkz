from quarkz.utils import createKey 
from decimal import Decimal
from quarkz.rsa import encrypt, decrypt
import decimal
decimal.getcontext().prec=5000
pair = createKey(keysize=1024)
pubKey = pair.get_public_key() 
o = pubKey["o"]
ratio = pubKey["ratio"]
fraction = Decimal(ratio).as_integer_ratio()
print("fraction: ", fraction)
a, b = fraction
while (a > Decimal('1e2000')):
    a, b = b % a, a
n = ((Decimal(fraction[1]) / b) + o).quantize(Decimal(1))

# print ("FOUND DIFF: ", Decimal(fraction[1]) / b)

print ("FOUND N: ", n)
