from decimal import Decimal

class Encrypted(dict):
    def __init__(self, ciphertext: Decimal, offsetCount: Decimal):
        ''' All values are read only '''
        self._ciphertext = ciphertext
        self._offsetCount = offsetCount

    def __str__(self):
        return f"quarkz.Encryption object @ {self._offsetCount}"
    
    @property
    def __dict__(self):
        return {"ciphertext": self._ciphertext, "offset": self._offsetCount}


