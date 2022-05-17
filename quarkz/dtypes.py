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


class KeyPair():
    def __init__(self, public_key: dict, private_key: dict) -> None: 
        self._pub = public_key
        self.__priv = private_key #private to class

    @property
    def __dict__(self):
        return {"publicKey": self._pub, "privateKey": self.__priv}

    def get_public_key(self):
        return self._pub

    def get_private_key(self):
        return self.__priv


