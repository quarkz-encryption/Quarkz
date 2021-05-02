#from utils import gcd, egcd, modpow, mod_inverse

''' Ensures that values are calculated as expected '''

def test_gcd():
    from quarkz.utils import gcd
    assert (gcd(88, 99) == 11) 

def test_egcd():
    from quarkz.utils import egcd
    assert((11, 1, -1) == egcd(99, 88))

def test_mod_inverse():
    from quarkz.utils import mod_inverse
    assert(mod_inverse(32, 21) == 2)
    
