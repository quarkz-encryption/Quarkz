import decimal

class Encrypted(dict):
    def __init__(self, e: decimal.Decimal, m: decimal.Decimal, o: decimal.Decimal, d: decimal.Decimal, priv: int, pub: int, n: decimal.Decimal):
        ''' All values are read only '''
        self._e = e
        self._m = m 
        self._o = o 
        self._d = d 
        self._priv = priv 
        self._pub = pub 
        self._n = n 

    def __str__(self):
        return f"quarkz.Encryption object @ {self._pub}"
    
    @property
    def __dict__(self):
        return {"e": self._e, "m": self._m, "o": self._o, "d": self._d, "priv": self._priv, "pub": self._pub, "n": self._n}


